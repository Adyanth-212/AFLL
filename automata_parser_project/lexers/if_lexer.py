import ply.lex as lex

tokens = ('IF', 'ID', 'NUMBER', 'LPAREN', 'RPAREN', 'LT', 'GT', 'EQ', 'NE')

t_IF = r'if'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NE = r'!='
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
