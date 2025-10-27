import ply.lex as lex

tokens = ('LBRACE', 'RBRACE', 'NUMBER', 'COMMA')

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
