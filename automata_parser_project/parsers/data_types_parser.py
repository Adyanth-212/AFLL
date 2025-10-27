# parsers/data_types_parser.py
import ply.yacc as yacc
from ..lexers.data_types_lexer import tokens

def p_data_type(p):
    """
    data_type : INTEGER
              | FLOAT
              | STRING
              | BOOLEAN
              | COMPLEX
              | NONE
    """
    p[0] = p[1]

def p_error(p):
    if p:
        print("❌ Syntax error in data type")
    else:
        print("❌ Syntax error: Incomplete data type")

parser = yacc.yacc(tabmodule='data_types_parsetab')
