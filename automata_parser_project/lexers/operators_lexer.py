# lexers/operators_lexer.py
import ply.lex as lex

tokens = (
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'FLOORDIV', 'MODULO', 'POWER',
    'EQ', 'NE', 'GT', 'LT', 'GE', 'LE',
    'AND', 'OR', 'NOT',
    'EQUALS', 'PLUSEQUALS', 'MINUSEQUALS',
    'LPAREN', 'RPAREN',
)

t_ignore = ' \t\n'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_FLOORDIV = r'//'
t_MODULO = r'%'
t_POWER = r'\*\*'

t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='

t_EQUALS = r'='
t_PLUSEQUALS = r'\+='
t_MINUSEQUALS = r'-='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in ('and', 'or', 'not'):
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
