import re
from ClaseVariable import Variable
#from Instrucciones import variables
from Variables import variables
import sys

par=re.compile("\(")
class QNode:
    def __init__(self,data):
        self.next = None
        self.data = data
    
    def __str__(self):
        s = str(self.data)
        
        return s
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def push(self,data):
        n = QNode(data)
        if self.first is None:
            self.first=n
            self.last=n
        else:
            aux=self.last
            aux.next=n
            self.last=n;
    def top(self):
        if self.first is not None:
            return self.first.data
        else:
            return None
    def pop(self):
        if self.first is not None:
            aux=self.first.data
            self.first=self.first.next
            return aux
        else:
            return None
    def isEmpty(self):
        if(self.first is None):
            return True
        else:
            return False
        

class SNode:
    def __init__(self,data):
        self.next = None
        self.data = data
    
    def __str__(self):
        s = str(self.data)
        return s
class Stack:
    def __init__(self):
        self.first = None
    def push(self,data):
        n=SNode(data)
        if self.first is None:
            self.first=n
        else:
            n.next=self.first
            self.first=n
    def pop(self):
        if self.first is not None:
            aux=self.first.data
            self.first=self.first.next
            return aux
        else:
            return None
    def top(self):
        if self.first is not None:
            return self.first.data
        else:
            return None
    def isEmpty(self):
        if(self.first is None):
            return True
        else:
            return False


class Token:
    def __init__(self,valor,operator):
        self.valor=valor
        self.operator=operator
        if self.operator:
            if self.valor=="(" or self.valor==")":
                self.priori=7
            elif valor== "✖️" or valor=="➗":
                self.priori=6
            elif valor=="➕" or valor=="➖":
                self.priori=5
            elif valor=="▶️" or valor=="◀️" or valor =="▶️⏸" or valor=="◀️⏸" or valor=="⏸" or valor=="🚫⏸":
                self.priori=4
            elif valor=="🚫":
                self.priori=3
            elif valor=="🅰️":
                self.priori=2
            elif valor=="🅾️":
                self.priori=1
            else:
                print("ERROR: Algo salió mal")
                self.priori=0
        
        else:
            self.priori=0
    def isOperator(self):
        return self.operator
    def getValor(self):
        return self.valor
    def getPriori(self):
        return self.priori
    def __str__(self):
        s=""
        s+=str(self.valor)
        s+=": p="
        s+=str(self.priori)
        return s
    
def esNumero(cadena):
    punto=False
    for i in range(0,len(cadena)):
        if cadena[i].isnumeric():
            pass
        elif cadena[i]==".":
            if punto:
                return False
            else:
                punto=True
        elif cadena[i]=="-" and i==0:
            pass
        else:
            return False
    return True

def Operacion(op1,op,op2):
    a=op1.getValor()
    b=op2.getValor()
    c=0
    if op.getValor()=="➕":
        c=a+b
    elif op.getValor()=="➖":
        c=a-b
        
    elif op.getValor()=="✖️":
        c=a*b
    elif op.getValor()=="➗":
        c=a/b
    elif op.getValor()=="▶️":
        if a>b:
            c=1
        else:
            c=0
    elif op.getValor()=="◀️":
        if a<b:
            c=1
        else:
            c=0
    elif op.getValor()=="▶️⏸":
        if a>=b:
            c=1
        else:
            c=0
    elif op.getValor()=="◀️⏸":
        if a<=b:
            c=1
        else:
            c=0
    elif op.getValor()=="⏸":
        if a==b:
            c=1
        else:
            c=0
    elif op.getValor()=="🚫⏸":
        if a!=b:
            c=1
        else:
            c=0
    elif op.getValor()=="🅰️":
        if a!=0 and b!=0:
            c=1
        else:
            c=0
    elif op.getValor()=="🅾️":
        if a!=0 or b!=0:
            c=1
        else:
            c=0
    tkaux=Token(c,False)
    return tkaux

def Negar(op1):
    a=op1.getValor()
    if a!=0:
        c=0
    else:
        c=1
    tkaux=Token(c,False)
    
    return tkaux
    
        

def Evaluador(instruccion):
    #print('Hello')
    cadena=instruccion
    cadenamod=re.sub(r"\("," ( ",cadena)
    cadenamod=re.sub(r"\)"," ) ",cadenamod)
    cadenamod=re.sub(r'[^a-zA-Z0-9()➕➖➗✖️▶️◀️🚫🅰️🅾️⏸✅❌.[^,] *]{2,10000}',' ',cadenamod)
    #print(cadenamod)
    cadarr=cadenamod.split()
    d_tokens=dict()
    for i in range(0,len(cadarr)):
        if(cadarr[i]=="➕" or cadarr[i]=="➖" or cadarr[i]=="✖️"or cadarr[i]=="➗" or cadarr[i]=="▶️"or cadarr[i]=="◀️"or cadarr[i]=="▶️⏸"or cadarr[i]=="◀️⏸"or cadarr[i]=="⏸"or cadarr[i]=="🚫⏸"or cadarr[i]=="🅰️"or cadarr[i]=="🅾️"or cadarr[i]=="🚫" or cadarr[i]=="("or cadarr[i]==")"):
            tk=Token(cadarr[i],True)
            d_tokens[i]=tk
        elif cadarr[i]=="✅":
            tk=Token(1,False)
            d_tokens[i]=tk
        elif cadarr[i]=="❌":
            tk=Token(0,False)
            d_tokens[i]=tk   
        else:
            if(esNumero(cadarr[i])):
                tk=Token(float(cadarr[i]),False)
                d_tokens[i]=tk
                
            else:
                if cadarr[i] in variables.keys():
                    if variables[cadarr[i]].getTipo()==str:
                        print("ERROR: No es posible hacer operaciones con Texto")
                        sys.exit(1)
                    else:
                        tk=Token(variables[cadarr[i]].getDato(),False)
                        d_tokens[i]=tk
                else:
                    print('ERROR: "{}" no se reconoce como variable o numero valido.'.format(cadarr[i]))
                    sys.exit(1)
        
                
            
    stackO= Stack()
    queueF= Queue()
    
    
    for i in d_tokens:
        #print(d_tokens[i])
        if d_tokens[i].isOperator():
            if d_tokens[i].getValor() ==")":
                while(True):
                    if stackO.isEmpty():
                        print("ERROR: Error semantico.")
                        sys.exit(1)
                    else:
                        if stackO.top().getValor()!="(":
                            queueF.push(stackO.pop())
                        else:
                            stackO.pop()
                            break
            else:
                if stackO.isEmpty()==False: 
                    while(stackO.top().getPriori()>= d_tokens[i].getPriori() and stackO.top().getValor()!="("):
                        queueF.push(stackO.pop())
                        if stackO.isEmpty():
                            break
                stackO.push(d_tokens[i])
        else:
            queueF.push(d_tokens[i])
    while stackO.isEmpty()==False:
        queueF.push(stackO.pop())
        
        
    stackF=Stack()
    while(queueF.isEmpty()==False):
        if queueF.top().isOperator() and queueF.top().getValor()!="🚫":
            if stackF.isEmpty():
                print("ERROR: Algo salio mal.")
                sys.exit(1)
            else:
                op2=stackF.pop()
                if stackF.isEmpty():
                    print("ERROR: Algo salio mal")
                    sys.exit(1)
                else: 
                    op1=stackF.pop()
            tkaux=Operacion(op1,queueF.pop(),op2)
            stackF.push(tkaux)
        elif queueF.top().isOperator() and queueF.top().getValor()=="🚫":
            if stackF.isEmpty():
                print("ERROR: Algo salio mal")
                sys.exit(1)
            else:
                op1=stackF.pop()
                queueF.pop()
                tkaux=Negar(op1)
                stackF.push(tkaux)
        else:
            stackF.push(queueF.pop())
    tkfinal=stackF.pop()
    if stackF.isEmpty()==False:
        print("ERROR: Algo salio mal")
        sys.exit(1)
    #print(tkfinal.getValor())
    return tkfinal.getValor()


'''
print(Evaluador('100 ▶️ 50'))
print(Evaluador('✅'))
print(Evaluador('✅ 🅰️ (✅ 🅾️ ❌)'))
'''
        
                