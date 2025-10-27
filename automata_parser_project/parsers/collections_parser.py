# parsers/collections_parser.py
import ply.yacc as yacc
from ..lexers.collections_lexer import tokens

def p_declaration(p):
    """
    declaration : ID EQUALS collection
    """
    p[0] = ('=', p[1], p[3])

def p_collection(p):
    """
    collection : list
               | tuple
               | set
               | dict
    """
    p[0] = p[1]

# List parsing
def p_list(p):
    """
    list : LBRACKET items RBRACKET
         | LBRACKET RBRACKET
    """
    p[0] = ('list', p[2] if len(p) > 3 else [])

# Tuple parsing
def p_tuple(p):
    """
    tuple : LPAREN items RPAREN
          | LPAREN RPAREN
    """
    p[0] = ('tuple', p[2] if len(p) > 3 else [])

# Set parsing
def p_set(p):
    """
    set : LBRACE items RBRACE
    """
    p[0] = ('set', p[2])

# Dictionary parsing
def p_dict(p):
    """
    dict : LBRACE pairs RBRACE
         | LBRACE RBRACE
    """
    p[0] = ('dict', p[2] if len(p) > 3 else {})

def p_items(p):
    """
    items : item
          | items COMMA item
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_item(p):
    """
    item : STRING
         | NUMBER
    """
    p[0] = p[1]

def p_pairs(p):
    """
    pairs : pair
          | pairs COMMA pair
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_pair(p):
    """
    pair : STRING COLON item
    """
    p[0] = (p[1], p[3])

def p_error(p):
    if p:
        print(f"❌ Syntax error in collection at '{p.value}'")
    else:
        print("❌ Syntax error in collection: Incomplete statement")

parser = yacc.yacc(tabmodule='collections_parsetab')
