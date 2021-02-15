from ClaseVariable import Variable
from RegexLine import regexLines
from Evaluador import Evaluador
import re, sys
from Variables import variables

ultimaCondicionEvaluada = False # NO MODIFICAR

imprimirAuxiliares = False 

def analizador(text): # Recibe una cadena de texto
    errores_str = ''
    errores_int = 0
    lines = text.split('\n')
    i = 0

    while i < len(lines):
        if lines[i].strip() == '' or lines[i].strip() == '🍉': 
            i += 1
        else:

            notInRegexs = True
            
            for token, r in regexLines.items():
                try:
                    if r.regex.fullmatch(lines[i].strip()):
                        instruccion = r.regex.fullmatch(lines[i].strip())
                        tokenAuxiliarStr = 'Token ' + str(token) + ': ' + instruccion.group()
                        print(tokenAuxiliarStr + ' ' * (60 - len(tokenAuxiliarStr)) + '¡Valido!') if imprimirAuxiliares else None
                        notInRegexs = False
                        
                        scope_aux = []
                        if r.scoped:
                            while True:
                                i+=1

                                if lines[i] == '🍉':
                                    scope_aux.append(lines[i].strip())
                                    break

                                if lines[i][0] == '🍉':
                                    break

                                print('Scope: ' + lines[i]) if imprimirAuxiliares else None
                                scope_aux.append(lines[i].strip())

                        instrucciones[token](instruccion, scope_aux) # Llamada a evaluar la función
                        #break
                except IndexError:
                    print('ERROR: Linea {} carece de un elemento.'.format(i))
                    sys.exit(1)

                        
            if notInRegexs:
                errores_str += 'ERROR: Lexico invalido, linea {}: {}\n'.format(i+1,lines[i])
                errores_int += 1
                return errores_int, errores_str
            #print([variable.__str__() for variable in variables.values()]) if imprimirAuxiliares else None
            i += 1

    return errores_int, errores_str

def escribir(instruccion, scope): # Recibe un Match Object de regex
    if instruccion.group('Texto'):
        print(instruccion.group('Texto'))

    elif instruccion.group('Variable'):
        v = instruccion.group('Variable')
        try:
            print( str( variables[v] ) )
        except:
            print('ERROR: No existe la variable', v)

    elif instruccion.group('Operacion'):
        #print('Pasando {} al evaluador.'.format(instruccion.group('Operacion')))
        print(Evaluador(instruccion.group('Operacion')))

def declarar(instruccion, scope): # Recibe un Match Object de regex
    varAux = instruccion.group('Variables').replace(' ','')
    nombres_de_variables = varAux.split(',')
    tipo_de_dato = instruccion.group('DataType')
    
    for nombre in nombres_de_variables:
        if nombre in variables.keys():
            print('ERROR: Variable "{}" declarada previamente.'.format(nombre))
            sys.exit(1)
        variables[nombre] = Variable(nombre, tipo_de_dato)

def leer(instruccion, scope): # Recibe un Match Object de regex
    nombre_de_variable = instruccion.group('Variable')
    try:
        
        variable = variables[nombre_de_variable]
        tipo_de_dato = variable.tipo_de_dato
        
        try:
            if tipo_de_dato == int:
                valor = int(input())
            elif tipo_de_dato == float:
                valor = float(input())
            elif tipo_de_dato == str:
                valor = input()
            elif tipo_de_dato == bool:
                valor = input()
                if valor == '✅':
                    valor = True
                elif valor == '❌':
                    valor = False
            
            variable.setDato(valor)
        except:
            print('ERROR: Valor introducido no coincide con tipo',tipo_de_dato)
            sys.exit(1)
    except KeyError as e:
        print('ERROR: Variable "{}" no definida o referenciada antes de la declaracion.'.format(nombre_de_variable))
        sys.exit(1)

def igualar(instruccion, scope): # PENDIENTE Recibe un Match Object de regex
    nombre_de_variable = instruccion.group('Variable_a_igualar')
    try:
        if instruccion.group('Texto'):
            variables[nombre_de_variable].setDato(instruccion.group('Texto'))

        elif instruccion.group('Numero'):
            variables[nombre_de_variable].setDato(instruccion.group('Numero'))

        elif instruccion.group('Variable'):
            print(instruccion.group('Variable'))
            variables[nombre_de_variable].setDato(variables[ instruccion.group('Variable') ].getDato())

        elif instruccion.group('Operacion'):
            
            variables[nombre_de_variable].setDato(Evaluador(instruccion.group('Operacion')))
    except KeyError as ke:
        print('ERROR: Variable "{}" no definida o referenciada antes de la declaracion.'.format(nombre_de_variable))
        sys.exit(1)

def si(instruccion, scope): # PENDIENTE Recibe un Match Object de regex
    global ultimaCondicionEvaluada
    ultimaCondicionEvaluada = False
    if Evaluador(instruccion.group('Operacion')):
        analizador('\n'.join(scope))
        ultimaCondicionEvaluada = True

def o_si(instruccion, scope): # PENDIENTE Recibe un Match Object de regex
    global ultimaCondicionEvaluada
    if not ultimaCondicionEvaluada and Evaluador(instruccion.group('Operacion')):
        analizador('\n'.join(scope))
        ultimaCondicionEvaluada = True

def sino(instruccion, scope): # PENDIENTE Recibe un Match Object de regex
    global ultimaCondicionEvaluada
    if not ultimaCondicionEvaluada:
        analizador('\n'.join(scope))
        ultimaCondicionEvaluada = False

def mientras(instruccion, scope): # PENDIENTE Recibe un Match Object de regex
    LIMITE_DE_CICLO = 1000
    vuelta = 0
    while Evaluador(instruccion.group('Operacion')):
        if vuelta >= LIMITE_DE_CICLO:
            print('ERROR: Limite maximo de ciclo alcanzado.')
            sys.exit(1)
        analizador('\n'.join(scope))
        vuelta += 1

def de(instruccion, scope): #  Recibe un Match Object de regex
    variable_principal = instruccion.group('VariablePrincipal')
    numero_inicial = int(instruccion.group('NumeroInicial')) if instruccion.group('NumeroInicial') else variables[instruccion.group('VariableInicial')].getDato()
    numero_final = int(instruccion.group('NumeroFinal')) if instruccion.group('NumeroFinal') else variables[instruccion.group('VariableFinal')].getDato()
    numero_paso = int(instruccion.group('NumeroPaso')) if instruccion.group('NumeroPaso') else variables[instruccion.group('VariablePaso')].getDato()
    
    if variable_principal in variables.keys():
            print('ERROR: Variable "{}" declarada previamente.'.format(variable_principal))
            sys.exit(1)
    if numero_paso == 0:
        print('ERROR: El paso no puede ser de 0.')
        sys.exit(1)

    variables[variable_principal] = Variable(variable_principal,'🔢')
    variables[variable_principal].setDato(numero_inicial)
    for _ in range(numero_inicial, numero_final, numero_paso):
        analizador('\n'.join(scope))
        variables[variable_principal].setDato(variables[variable_principal].getDato() + numero_paso)
    variables.pop(variable_principal)

def comentario(instruccion, scope):
    return

instrucciones = {
    11: declarar,
    12: igualar,
    13: escribir,
    14: leer,
    15: si,
    16: o_si,
    17: sino,
    18: de,
    19: mientras,
    20: comentario }

