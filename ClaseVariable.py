import sys

class Variable:
    def __init__(self, nombre_de_variable, tipo_de_dato):
        self.nombre_de_variable = nombre_de_variable

        if tipo_de_dato == "🔢":
            self.tipo_de_dato = int
            self.dato = 0
        elif tipo_de_dato == "🔤":
            self.tipo_de_dato =str
            self.dato = ""
        elif tipo_de_dato == "🆗":
            self.tipo_de_dato = bool
            self.dato = False
        elif tipo_de_dato == "⏺":
            self.tipo_de_dato =float
            self.dato = 0.0
        else:
            print("ERROR: Tipo de dato no reconocido.")
        self.error=False
        
        
    def getNombre(self):
        return self.nombre_de_variable
    def getTipo(self):
        return self.tipo_de_dato
    def getDato(self):
        return self.dato
    def getError(self):
        return self.error
    def setDato(self,dato):
        if self.tipo_de_dato is int:
            try:
                self.dato=int(dato)
            except:
                self.error=True
                print('ERROR: Valor introducido no coincide con tipo entero.')
                sys.exit(1)
        elif self.tipo_de_dato is float:
            try:
                self.dato=float(dato)
            except:
                self.error=True
                print('ERROR: Valor introducido no coincide con tipo flotante.')
                sys.exit(1)
        elif self.tipo_de_dato is bool:
            try:
                self.dato=bool(dato)
            except:
                self.error=True
                print('ERROR: Valor introducido no coincide con tipo condicional.')
                sys.exit(1)
        else:
            self.dato=str(dato)

    def __str__(self):
        s=""
        #s+=str(self.nombre_de_variable)
        #s+=": "
        s+=str(self.dato)
        return s