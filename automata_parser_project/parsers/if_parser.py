import ply.yacc as yacc
from ..lexers.if_lexer import tokens

def p_if_statement(p):
    'if_statement : IF LPAREN condition RPAREN'
    p[0] = ('if', p[3])

def p_condition(p):
    '''condition : ID LT NUMBER
                 | ID GT NUMBER
                 | ID EQ NUMBER
                 | ID NE NUMBER'''
    p[0] = (p[2], p[1], p[3])

def p_error(p):
    print("❌ Syntax error in if construct")

parser = yacc.yacc(tabmodule='if_parsetab')
