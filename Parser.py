from Lexer import tokens
import ply.yacc as yacc
import math

padding: int = 0 # para acertar contas, isto vai dar trabalho

# pad = lambda x: 1. if x != 0 else x * 10

# yacc
def p_expressao_SOMA(p):
    'expressao : expressao SOMA termo'
    p[0] = p[1] + p[3]

def p_expressao_SUB(p):
    'expressao : expressao SUB termo'
    p[0] = p[1] - p[3]

def p_expressao_termo(p):
    'expressao : termo'
    p[0] = p[1]

def p_termo_PROD(p):
    'termo : termo PROD fator'
    p[0] = p[1] * p[3]

def p_termo_PROD_PARENTESIS(p):
    'termo : termo LPAR expressao RPAR'
    p[0] = p[1] * p[3]

def p_termo_DIV(p):
    'termo : termo DIV fator'
    p[0] = p[1] / p[3]

def p_termo_fator(p):
    'termo : fator'
    p[0] = p[1]

def p_termo_POTENCIA(p):
    'fator : fator POTENCIA num'
    p[0] = p[1] ** p[3]

def p_termo_RAIZ(p):
    'fator : num RAIZ fator'
    p[0] = p[3] ** (1./p[1])

def p_termo_FRAC(p):
    'fator : num FRAC fator'
    p[0] = p[1] / p[3]

def p_termo_SQRT(p):
    'fator : RAIZ num'
    p[0] = p[2] ** 0.5

def p_FACTORIAL(p):
    'fator : num FACT'
    r: float = 1.
    if p[1] == 0:
        p[0] = 1.
    else:
        while p[1] != 1.:
            r *= p[1]
            p[1] -= 1.
        p[0] = r

def p_fator_num(p):
    'fator : num'
    p[0] = p[1]

def p_expressao_PARENTESIS(p):
    'num : LPAR expressao RPAR'
    p[0] = p[2]

def p_number_NUMBER(p):
    'num : NUMBER'
    p[0] = p[1]

def p_number_PI(p):
    'num : PI'
    p[0] = math.pi

def p_error(p):
    print("Formato de expressão inválido!")

def parse(expression):
    return yacc.yacc().parse(expression)