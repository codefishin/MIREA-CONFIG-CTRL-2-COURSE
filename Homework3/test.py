import unittest
import json
from gen import CodeGenerator

class TestCodeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = CodeGenerator()

    def test_number(self):
        json_data = 42
        output = self.generator.generate(json_data)
        self.assertEqual(output, '42')

    def test_string(self):
        json_data = "Hello, World!"
        output = self.generator.generate(json_data)
        self.assertEqual(output, '"Hello, World!"')

    def test_array(self):
        json_data = [1, 2, 3]
        output = self.generator.generate(json_data)
        self.assertEqual(output, '<< 1, 2, 3 >>')

    def test_nested_array(self):
        json_data = [1, [2, 3], 4]
        output = self.generator.generate(json_data)
        self.assertEqual(output, '<< 1, << 2, 3 >>, 4 >>')

    def test_dictionary(self): # !!!!!!!!!!
        json_data = {
            "key1": "value1",
            "key2": 42,
            "key3": [1, 2, 3]
        }
        output = self.generator.generate(json_data)
        expected_output = '''{
  key1 : "value1",
  key2 : 42,
  key3 : << 1, 2, 3 >>
}'''
        self.assertEqual(output, expected_output)

    def test_nested_dictionary(self):
        json_data = {
            "outer_key": {
                "inner_key": "inner_value"
            }
        }
        output = self.generator.generate(json_data)
        expected_output = '''{
  outer_key : {
  inner_key : "inner_value"
}
}'''
        self.assertEqual(output, expected_output)

    def test_constant_declaration(self):
        json_data = {
            "PI <-": 3.14
        }
        output = self.generator.generate(json_data)
        expected_output = '{\n  PI <- 3.14\n}'
        self.assertEqual(output, expected_output)

    def test_constant_expression(self):
        json_data = {
            "expr": ["+", 1, 2]
        }
        result = self.generator.evaluate(json_data)
        self.assertEqual(result, 3)

    def test_constant_expression_generation(self):
        json_data = {
            "^(+ x 1)": 0
        }
        self.generator.constants['x'] = 5
        with self.assertRaises(ValueError):
            self.generator.generate(json_data)

    def test_invalid_identifier(self):
        json_data = {
            "123invalid": "value"
        }
        with self.assertRaises(ValueError):
            self.generator.generate(json_data)

    def test_example_nested(self):
        json_data = {
            "config": {
                "data": [1, 2, {"nested": "value"}]
            }
        }
        output = self.generator.generate(json_data)
        expected_output = '''{
  config : {
  data : << 1, 2, {
  nested : "value"
} >>
}
}'''
        self.assertEqual(expected_output,output)

    def test_unknown_operator(self):
        json_data = {
            "expr": ["unknown_op", 1, 2]
        }
        with self.assertRaises(ValueError):
            self.generator.evaluate(json_data)

if __name__ == '__main__':
    unittest.main()