import math
import sys
from node import *

class CodeGenerator:
    def __init__(self):
        self.constants = {}  # For constant declarations and evaluations

    def generate(self, data):
        return self.visit(data)

    def visit(self, node):
        if isinstance(node, dict):
            return self.visit_dict(node)
        elif isinstance(node, list):
            return self.visit_list(node)
        elif isinstance(node, str):
            return self.visit_string(node)
        elif isinstance(node, (int, float)):
            return self.visit_number(node)
        else:
            raise ValueError(f"Unsupported data type: {type(node)}")

    def visit_number(self, node):
        return str(node)

    def visit_string(self, node):
        return f'"{node}"'

    def visit_list(self, node):
        elements = []
        for item in node:
            elements.append(self.visit(item))
        return f"<< {', '.join(elements)} >>"

    def visit_dict(self, node):
        # Check for special keys indicating constant declarations or expressions
        output_lines = []

        for key, value in node.items():
            # Handle constant declaration
            if key.endswith('<-'):
                const_name = key[:-2].strip()
                self.constants[const_name] = self.evaluate(value)
                output_lines.append(f"{const_name} <- {self.visit_constant_value(value)}")
            # Handle constant expression
            elif key.startswith('^(') and key.endswith(')'):
                expr = key[1:]  # Remove leading '^'
                result = self.evaluate_expression(expr)
                output_lines.append(str(result))
            else:
                # Regular key-value pair
                key_str = key
                if not self.is_valid_identifier(key_str):
                    raise ValueError(f"Invalid identifier: {key_str}")
                value_str = self.visit(value)
                output_lines.append(f"{key_str} : {value_str}")

        return "{\n  " + ",\n  ".join(output_lines) + "\n}"

    def visit_constant_value(self, value):
        # Evaluate the value for constant declaration
        result = self.evaluate(value)
        if isinstance(result, str):
            return f'"{result}"'
        else:
            return str(result)

    def is_valid_identifier(self, name):
        import re
        return re.match(r'^[_a-zA-Z]+', name) is not None
    # Имена:
    # [_a-zA-Z]+

    def evaluate(self, node):
        if isinstance(node, dict):
            # Handle constant expression
            if 'expr' in node:
                expr = node['expr']
                return self.evaluate_expression(expr)
            else:
                raise ValueError("Invalid constant expression")
        else:
            # Return the value as is
            return node

    def evaluate_expression(self, expr):
        # Assume expr is a list in prefix notation
        if not isinstance(expr, list):
            raise ValueError("Expression must be a list in prefix notation")
        operator = expr[0]
        operands = expr[1:]

        evaluated_operands = [self.resolve_operand(op) for op in operands]

        if operator == '+':
            return sum(evaluated_operands)
        elif operator == '-':
            if len(evaluated_operands) == 1:
                return -evaluated_operands[0]
            elif len(evaluated_operands) == 2:
                return evaluated_operands[0] - evaluated_operands[1]
            else:
                raise ValueError("Subtraction requires 1 or 2 operands")
        elif operator == '*':
            result = 1
            for op in evaluated_operands:
                result *= op
            return result
        elif operator == '/':
            if len(evaluated_operands) != 2:
                raise ValueError("Division requires exactly 2 operands")
            return evaluated_operands[0] / evaluated_operands[1]
        elif operator == 'sqrt':
            if len(evaluated_operands) != 1:
                raise ValueError("sqrt requires exactly 1 operand")
            return math.sqrt(evaluated_operands[0])
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def resolve_operand(self, operand):
        if isinstance(operand, str):
            # Could be a constant
            if operand in self.constants:
                return self.constants[operand]
            else:
                # Try to parse as number
                try:
                    return float(operand)
                except ValueError:
                    raise ValueError(f"Unknown identifier: {operand}")
        elif isinstance(operand, (int, float)):
            return operand
        else:
            raise ValueError(f"Invalid operand type: {type(operand)}")