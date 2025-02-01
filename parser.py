import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS'
)

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Reglas de los tokens
t_ignore = ' \t'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Reglas de la gramática
def p_statement_assign(p):
    'statement : ID EQUALS expression'
    print(f"Asignación: {p[1]} = {p[3]}")

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3] if p[3] != 0 else "Error: División por cero"

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()

# Pruebas
def run_parser():
    while True:
        try:
            s = input('>> ')
        except EOFError:
            break
        if not s:
            continue
        parser.parse(s)

if __name__ == '__main__':
    run_parser()
