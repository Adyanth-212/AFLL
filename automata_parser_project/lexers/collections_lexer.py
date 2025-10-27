# lexers/collections_lexer.py
import ply.lex as lex

tokens = (
    'ID', 'EQUALS',
    'LBRACKET', 'RBRACKET',  # List
    'LPAREN', 'RPAREN',      # Tuple
    'LBRACE', 'RBRACE',      # Set, Dict
    'COMMA', 'COLON',
    'STRING', 'NUMBER',
)

t_ignore = ' \t\n'

t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
