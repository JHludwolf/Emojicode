import re, sys
from Instrucciones import instrucciones, analizador, imprimirAuxiliares

if __name__ == "__main__":
    testCodeText = open('testCode.txt','r').read()
    testCodeText4 = open('testCode4.txt','r').read()

    numero_errores, string_errores = analizador(testCodeText)

    if numero_errores == 0:
        print('¡Lexico Valido!') if imprimirAuxiliares else None
    else:
        print('{} {} lexico:'.format(numero_errores, 'error' if numero_errores == 1 else 'errores'))
        print(string_errores)