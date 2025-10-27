# lexers/loops_lexer.py
import ply.lex as lex

# This lexer is very similar to the selection lexer, as it also handles indentation.
tokens = (
    'WHILE', 'FOR', 'IN', 'RANGE', 'COLON', 'NEWLINE',
    'ID', 'NUMBER',
    'LPAREN', 'RPAREN',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE',
    'INDENT', 'DEDENT',
    'PRINT', 'STRING', 'PLUSEQUALS'
)

keywords = {
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'print': 'PRINT'
}

t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='
t_PLUSEQUALS = r'\+='
t_ignore = ' '

# A queue for pending tokens
token_queue = []
# Keeps track of indentation levels
indent_stack = [0]

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# The token wrapper to handle indentation
def token(lexer):
    if not token_queue:
        tok = lexer.token()

        if tok and tok.type == 'NEWLINE':
            line_start = lexer.lexdata.rfind('\n', 0, tok.lexpos) + 1
            indent_str = lexer.lexdata[line_start:tok.lexpos]
            indent_level = len(indent_str.replace('\t', '    '))

            if indent_level > indent_stack[-1]:
                indent_stack.append(indent_level)
                token_queue.append(_create_token('INDENT', tok.lineno))

            while indent_level < indent_stack[-1]:
                indent_stack.pop()
                token_queue.append(_create_token('DEDENT', tok.lineno))

        if not tok:
            while len(indent_stack) > 1:
                indent_stack.pop()
                token_queue.append(_create_token('DEDENT', lexer.lineno))
            if not token_queue:
                return None

        if tok:
            token_queue.append(tok)

    return token_queue.pop(0)

def _create_token(type, lineno):
    tok = lex.LexToken()
    tok.type = type
    tok.value = None
    tok.lineno = lineno
    tok.lexpos = 0
    return tok

# Build the lexer
lexer = lex.lex()
lexer.token = lambda: token(lexer)
