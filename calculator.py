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

Para mais informações escrever "help"|"h"''')
            continue
        elif expression in ('quit', 'q'):
            break
        elif expression in ('help', 'h'):
            print('''
********************
|                  |
|   py-calculator  |  by: acmota2
|                  |
********************

Esta calculadora permite calcular coisas segundo a regra PEMDAS com os seguintes operadores:
    +   : soma          (x + y)
    -   : subtração     (x - y)
    *   : multiplicação (x * y)
    /   : divisão       (x / y)
    ^   : potência      (x ^ y)
    v   : raiz          (x v y | v x)
    !   : fatorial      (x !)

É também possível efetuar operações do tipo "2(6 + 2)"
''')
            continue
        ans = yacc.parse(expression)
        print(ans)

__main__()