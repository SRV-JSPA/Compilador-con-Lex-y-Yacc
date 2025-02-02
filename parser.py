import ply.lex as lex
import ply.yacc as yacc

# Diccionario de variables
variables = {}

# ----------------------
# Analizador Léxico (Lex)
# ----------------------
tokens = (
    'NUMBER', 'ID'
)

# Literales
literals = ['+', '-', '*', '/', '=', ':']

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# ----------------------
# Analizador Sintáctico (Yacc)
# ----------------------
precedence = (
    ('right', '='),
    ('left', '+', '-'),
    ('left', '*', '/')
)

def p_program(p):
    '''program : statement_list'''
    pass

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    pass

def p_statement(p):
    '''statement : assignment
                 | expression ':' '''
    if len(p) == 3:
        print(f"Resultado: {p[1]}")

def p_assignment(p):
    '''assignment : ID '=' expression'''
    variables[p[1]] = p[3]
    print(f"Asignado: {p[1]} = {p[3]}")

def p_expression(p):
    '''expression : NUMBER
                  | ID
                  | expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if len(p) == 2:
        if isinstance(p[1], str):
            p[0] = variables.get(p[1], 0)
        else:
            p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3] if p[3] != 0 else print("Error: División por cero")

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()

# ----------------------
# Pruebas interactivas
# ----------------------
while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
