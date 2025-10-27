# parsers/loops_parser.py
import ply.yacc as yacc
from ..lexers.loops_lexer import tokens

def p_loop_statement(p):
    """
    loop_statement : while_loop
                   | for_loop
    """
    p[0] = p[1]

def p_while_loop(p):
    'while_loop : WHILE condition COLON suite'
    p[0] = ('while', p[2], p[4])

def p_for_loop(p):
    'for_loop : FOR ID IN RANGE LPAREN NUMBER RPAREN COLON suite'
    p[0] = ('for', p[2], p[6], p[9])

def p_suite(p):
    'suite : NEWLINE INDENT statements DEDENT'
    p[0] = p[3]

def p_statements(p):
    """
    statements : statement
               | statements statement
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    """
    statement : PRINT STRING NEWLINE
              | ID PLUSEQUALS NUMBER NEWLINE
    """
    if len(p) == 4:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[2], p[1], p[3])

def p_condition(p):
    """
    condition : ID GT NUMBER
              | ID LT NUMBER
              | ID GE NUMBER
              | ID LE NUMBER
              | ID EQ NUMBER
              | ID NE NUMBER
    """
    p[0] = (p[2], p[1], p[3])

def p_error(p):
    if p:
        print(f"❌ Syntax error in loop at '{p.value}' (type: {p.type})")
    else:
        print("❌ Syntax error in loop: Incomplete statement")

parser = yacc.yacc(tabmodule='loops_parsetab')
