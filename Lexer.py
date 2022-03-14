import ply.lex as lex

# List of token names
tokens = [
    'NUMBER',
    'SOMA',
    'SUB',
    'PROD',
    'DIV',
    'POTENCIA',
    'RAIZ',
    'FACT',
    'PI',
    'LPAR',
    'RPAR'
]

# operadores
literals = "+-*/^v!()"

# numeros
def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_SOMA(t):
    r'\+'
    return t

def t_SUB(t):
    r'-'
    return t

def t_PROD(t):
    r'\*'
    return t

def t_DIV(t):
    r'\/'
    return t

def t_POTENCIA(t):
    r'\^'
    return t

def t_RAIZ(t):
    r'v'
    return t

def t_FACT(t):
    r'\!'
    return t

def t_LPAR(t):
    r'\('
    return t

def t_RPAR(t):
    r'\)'
    return t

def t_PI(t):
    r'pi'
    return t

# ignorados
t_ignore = r' '

# erros
def t_error(t):
    print("Tenta outra vez. Inputs corretos incluem [NUMERO][OPERADOR][NUMERO]")
    t.lexer.skip(1)

lexer = lex.lex()