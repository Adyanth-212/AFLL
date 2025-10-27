from automata_parser_project.lexers.assignment_lexer import lexer as assignment_lexer
from automata_parser_project.parsers.assignment_parser import parser as assignment_parser
from automata_parser_project.lexers.expression_lexer import lexer as expression_lexer
from automata_parser_project.parsers.expression_parser import parser as expression_parser
from automata_parser_project.lexers.if_lexer import lexer as if_lexer
from automata_parser_project.parsers.if_parser import parser as if_parser
from automata_parser_project.lexers.while_lexer import lexer as while_lexer
from automata_parser_project.parsers.while_parser import parser as while_parser
from automata_parser_project.lexers.set_lexer import lexer as set_lexer
from automata_parser_project.parsers.set_parser import parser as set_parser

def main():
    while True:
        try:
            s = input('Enter a statement: ')
        except EOFError:
            break
        if not s:
            continue

        if s.startswith('int') or s.startswith('str'):
            result = assignment_parser.parse(s, lexer=assignment_lexer)
            if result:
                print("✅ Valid assignment statement")
        elif s.startswith('if'):
            result = if_parser.parse(s, lexer=if_lexer)
            if result:
                print("✅ Valid IF condition")
        elif s.startswith('while'):
            result = while_parser.parse(s, lexer=while_lexer)
            if result:
                print("✅ Valid WHILE condition")
        elif s.startswith('{'):
            result = set_parser.parse(s, lexer=set_lexer)
            if result:
                print("✅ Valid SET declaration")
        else:
            result = expression_parser.parse(s, lexer=expression_lexer)
            if result:
                print("✅ Valid arithmetic expression")

if __name__ == '__main__':
    main()
