# parsers/selection_parser.py
import ply.yacc as yacc
from ..lexers.selection_lexer import tokens

def p_selection_statement(p):
    """
    selection_statement : if_statement
                        | if_else_statement
    """
    p[0] = p[1]

def p_if_statement(p):
    'if_statement : IF condition COLON suite'
    p[0] = ('if', p[2], p[4])

def p_if_else_statement(p):
    """
    if_else_statement : IF condition COLON suite ELSE COLON suite
                      | IF condition COLON suite elif_statements ELSE COLON suite
                      | IF condition COLON suite elif_statements
    """
    if len(p) == 8: # if-elif-else
        p[0] = ('if-elif-else', p[2], p[4], p[5], p[7])
    elif len(p) == 6: # if-elif
        p[0] = ('if-elif', p[2], p[4], p[5])
    else: # if-else
        p[0] = ('if-else', p[2], p[4], p[7])

def p_elif_statements(p):
    """
    elif_statements : elif_statement
                    | elif_statements elif_statement
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_elif_statement(p):
    'elif_statement : ELIF condition COLON suite'
    p[0] = ('elif', p[2], p[4])

def p_suite(p):
    """
    suite : NEWLINE INDENT statements DEDENT
    """
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
    """
    p[0] = (p[1], p[2])

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
        print(f"❌ Syntax error in selection statement at '{p.value}' (type: {p.type})")
    else:
        print("❌ Syntax error in selection statement: Incomplete statement")

parser = yacc.yacc(tabmodule='selection_parsetab')
