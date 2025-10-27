# parsers/operators_parser.py
import ply.yacc as yacc
from ..lexers.operators_lexer import tokens

# Define precedence and associativity
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'EQ', 'NE', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'FLOORDIV', 'MODULO'),
    ('right', 'POWER'),
)

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    p[0] = ('=', p[1], p[3])

def p_statement_augassign(p):
    """
    statement : ID PLUSEQUALS expression
              | ID MINUSEQUALS expression
    """
    p[0] = (p[2], p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression FLOORDIV expression
               | expression MODULO expression
               | expression POWER expression
               | expression EQ expression
               | expression NE expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression AND expression
               | expression OR expression
    """
    p[0] = (p[2], p[1], p[3])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('not', p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"❌ Syntax error in operator expression at '{p.value}'")
    else:
        print("❌ Syntax error in operator expression: Incomplete statement")

parser = yacc.yacc(tabmodule='operators_parsetab')
