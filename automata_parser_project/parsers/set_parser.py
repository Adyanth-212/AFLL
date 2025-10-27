import ply.yacc as yacc
from ..lexers.set_lexer import tokens

def p_set_decl(p):
    'set_decl : LBRACE RBRACE'
    p[0] = ('set', [])

def p_set_decl_nonempty(p):
    'set_decl : LBRACE members RBRACE'
    p[0] = ('set', p[2])

def p_members(p):
    'members : NUMBER'
    p[0] = [p[1]]

def p_members_list(p):
    'members : members COMMA NUMBER'
    p[0] = p[1] + [p[3]]

def p_error(p):
    print("❌ Syntax error in set declaration")

parser = yacc.yacc(tabmodule='set_parsetab')
