'''
GRAMMAR

expressao   : expressao '+' termo
            | expressao '-' termo
            | termo
termo       : termo '*' fator
            | termo fator
            | termo '/' fator
            | fator
fator       : fator '^' num
            | num 'v' fator
            | 'v' num
            | '!' num
            | num
num         : NUMBER
            | '(' expressao ')'
'''

import Parser as yacc

def __main__():
    while(True):
        expression: str = input('input > ')
        if not expression:
            print('''Expressão nula e/ou vazia
Deverá receber um input do tipo [NUMERO][OPERADOR][NUMERO]''')
            continue
        elif expression == 'quit':
            break
        ans = yacc.parse(expression)
        print(ans)

__main__()