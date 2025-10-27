# lexers/selection_lexer.py
import ply.lex as lex

tokens = (
    'IF', 'ELIF', 'ELSE', 'COLON', 'NEWLINE',
    'ID', 'NUMBER', 'STRING',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE',
    'INDENT', 'DEDENT',
    'PRINT'
)

keywords = {'if': 'IF', 'elif': 'ELIF', 'else': 'ELSE', 'print': 'PRINT'}
t_COLON = r':'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='
t_ignore = ' '  # Ignore spaces within a line

# A queue for pending tokens (for DEDENT)
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
    # After a newline, we must check the indentation of the next line.
    # The logic is handled by the `token()` wrapper.
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# The main token function wrapper that handles indentation
def token(lexer):
    if not token_queue:
        # Get a token from the underlying lexer
        tok = lexer.token()

        if tok and tok.type == 'NEWLINE':
            # We're at the start of a new line, calculate the indentation
            line_start = lexer.lexdata.rfind('\n', 0, tok.lexpos) + 1
            indent_str = lexer.lexdata[line_start:tok.lexpos]

            # Assuming tabs are 4 spaces
            indent_level = len(indent_str.replace('\t', '    '))

            if indent_level > indent_stack[-1]:
                indent_stack.append(indent_level)
                token_queue.append(_create_token('INDENT', tok.lineno))

            while indent_level < indent_stack[-1]:
                indent_stack.pop()
                token_queue.append(_create_token('DEDENT', tok.lineno))

        # At the end of the file, we might need to dedent
        if not tok:
            while len(indent_stack) > 1:
                indent_stack.pop()
                token_queue.append(_create_token('DEDENT', lexer.lineno))
            if not token_queue:
                return None # End of tokens

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

# Build the lexer and wrap its token function
lexer = lex.lex()
lexer.token = lambda: token(lexer)
