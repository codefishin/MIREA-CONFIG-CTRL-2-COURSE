import argparse
import json
import sys
from conflang.gen import CodeGenerator


def main():
    parser = argparse.ArgumentParser(description='JSON to Educational Configuration Language Converter')
    parser.add_argument('--input', required=True, help='Path to the input JSON file')
    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
        sys.exit(1)

    code_generator = CodeGenerator()
    try:
        output = code_generator.generate(json_data)
        print(output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()