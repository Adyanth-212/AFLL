# test_custom.py
import re
from automata_parser_project.lexers.data_types_lexer import lexer as dt_lexer
from automata_parser_project.parsers.data_types_parser import parser as dt_parser
from automata_parser_project.lexers.operators_lexer import lexer as op_lexer
from automata_parser_project.parsers.operators_parser import parser as op_parser
from automata_parser_project.lexers.collections_lexer import lexer as col_lexer
from automata_parser_project.parsers.collections_parser import parser as col_parser
from automata_parser_project.lexers.selection_lexer import lexer as sel_lexer
from automata_parser_project.parsers.selection_parser import parser as sel_parser
from automata_parser_project.lexers.loops_lexer import lexer as loop_lexer
from automata_parser_project.parsers.loops_parser import parser as loop_parser

def is_data_type(s):
    # Simple check if it's a number, string, bool, etc.
    return re.match(r'^((\d+\.\d*)|(\d+)|(\"[^\"]*\")|True|False|None|(\d+\s*\+\s*\d+j))$', s.strip())

def is_collection(s):
    return s.strip().endswith((']', ')', '}'))

def main():
    print("Python Syntax Checker REPL")
    while True:
        try:
            # Read initial input
            s = input('>>> ')
            if not s:
                continue

            # Check for multi-line constructs
            if s.strip().endswith(':'):
                while True:
                    line = input('... ')
                    s += '\n' + line
                    # A simple heuristic to end multi-line input: an empty line.
                    if not line.strip():
                        break

            # Choose the right parser based on the input
            if 'if' in s or 'elif' in s or 'else' in s:
                result = sel_parser.parse(s, lexer=sel_lexer)
                if result:
                    print("✅ Valid selection statement syntax")
            elif 'while' in s or 'for' in s:
                result = loop_parser.parse(s, lexer=loop_lexer)
                if result:
                    print("✅ Valid loop syntax")
            elif '=' in s and (is_collection(s)):
                result = col_parser.parse(s, lexer=col_lexer)
                if result:
                    print("✅ Valid collection syntax")
            elif any(op in s for op in ['+', '-', '*', '/', '=', '==', 'and', 'or', 'not']):
                 result = op_parser.parse(s, lexer=op_lexer)
                 if result:
                     print("✅ Valid operator syntax")
            elif is_data_type(s):
                result = dt_parser.parse(s, lexer=dt_lexer)
                if result:
                    print("✅ Valid data type syntax")
            else:
                print("❌ Could not determine the construct type.")

        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
