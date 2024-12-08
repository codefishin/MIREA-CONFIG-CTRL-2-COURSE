# ast_nodes.py

class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class String(ASTNode):
    def __init__(self, value):
        self.value = value

class Array(ASTNode):
    def __init__(self, elements):
        self.elements = elements  # List of ASTNodes

class Dictionary(ASTNode):
    def __init__(self, pairs):
        self.pairs = pairs  # List of (key, value) tuples

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class ConstantDeclaration(ASTNode):
    def __init__(self, name, value):
        self.name = name  # Identifier
        self.value = value  # ASTNode

class ConstantExpression(ASTNode):
    def __init__(self, operator, operands):
        self.operator = operator  # String
        self.operands = operands  # List of ASTNodes