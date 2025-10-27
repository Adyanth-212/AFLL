# lexers/data_types_lexer.py
import ply.lex as lex

tokens = (
    'INTEGER', 'FLOAT', 'STRING', 'BOOLEAN', 'COMPLEX', 'NONE',
)

t_ignore = ' \t\n'

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = str(t.value[1:-1])  # Remove quotes
    return t

def t_BOOLEAN(t):
    r'True|False'
    t.value = t.value == 'True'
    return t

def t_COMPLEX(t):
    r'\d+\s*\+\s*\d+j'
    # A simple regex for complex numbers like "3 + 5j"
    t.value = complex(t.value.replace(" ", ""))
    return t

def t_NONE(t):
    r'None'
    t.value = None
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
