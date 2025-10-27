import ply.yacc as yacc
from ..lexers.assignment_lexer import tokens

def p_assignment(p):
    '''assignment : TYPE ID EQUALS value'''
    p[0] = ('assignment', p[2], p[4])

def p_value(p):
    '''value : NUMBER
             | STRING'''
    p[0] = p[1]

def p_error(p):
    print("❌ Syntax error in assignment")

parser = yacc.yacc(tabmodule='assignment_parsetab')
