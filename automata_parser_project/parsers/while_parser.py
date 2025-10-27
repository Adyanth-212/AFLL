import ply.yacc as yacc
from ..lexers.while_lexer import tokens

def p_while_statement(p):
    'while_statement : WHILE LPAREN condition RPAREN'
    p[0] = ('while', p[3])

def p_condition(p):
    '''condition : ID LT NUMBER
                 | ID GT NUMBER
                 | ID EQ NUMBER
                 | ID NE NUMBER'''
    p[0] = (p[2], p[1], p[3])

def p_error(p):
    print("❌ Syntax error in while construct")

parser = yacc.yacc(tabmodule='while_parsetab')
