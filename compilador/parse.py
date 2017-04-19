#from arbol import *
from Nodo import * 
#sintactico=open('sintactico.txt','w+')
i=0
reservadas=("main","if","then","else","end","do","while","repeat","until","cin","cout","real","int","boolean")

def printElement(element):
    print("",element)
    
def match(expectedToken):
    global i
    print("",tokens[i],"->",expectedToken)
    if tokens[i]==expectedToken:
        i+=1
    else:
        errorSintactico()

def errorSintactico():
    global i
    print("Syntax error en -> ",tokens[i])
    i+=1
        
def programa():
    global i
    nombre="main"
    raiz=Nodo(nombre)
    match("main")
    match('{')
    if tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
        p=listaDeclaracion()
        raiz.agregar_hijos(p)
    if tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
        q=listaSentencias()
        raiz.agregar_hijos(q)
    match('}')
    recorrer_arbol(raiz, 0)
          
def listaDeclaracion():
    global i
    temp=declaracion()
    match(';')
    if tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
        aux=declaracion()
        temp.agregar_hermano(aux)
        match(';')
        while tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
            q=aux
            aux=declaracion()
            q.agregar_hermano(aux)
            match(';')
    return temp

def declaracion():
    nombre=""
    global i
    if tokens[i]=="int":
          match("int")
          nombre="int"
          temp=Nodo(nombre)
          p=listaVariables()
          temp.agregar_hijos(p)
    if tokens[i]=="float":
          match("float")
          nombre="float"
          temp=Nodo(nombre)
          p=listaVariables()
          temp.agregar_hijos(p)
    if tokens[i]=="boolean":
          match("boolean")
          nombre="boolean"
          temp=Nodo(nombre)
          p=listaVariables()
          temp.agregar_hijos(p)
    return temp

def listaVariables():
    global i
    if es_id():
        nombre=str(tokens[i])
        i+=1
        temp=Nodo(nombre)
        match(',')
        if es_id():
            aux=Nodo(str(tokens[i]))
            temp.agregar_hermano(aux)
            i+=1
            if tokens[i]!=';':
                        match(',') 
            while tokens[i]!=';':
                q=aux
                if es_id():
                    hermano=str(tokens[i])
                    i+=1
                    aux=Nodo(hermano)
                    q.agregar_hermano(aux)
                    if tokens[i]!=';':
                        match(',')        
        return temp; 
    else:
          errorSintactico()     
          
          
def listaSentencias():
    global i
    temp=sentencias()
    if tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
        aux=sentencias()
        temp.agregar_hermano(aux)
        while tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
            q=aux
            aux=sentencias()
            q.agregar_hermano(aux)
    return temp

def es_id():
    global i
    texto=str(tokens[i])
    j=0
    n=0
    if texto[j].isalpha():
          while n < len(reservadas):
              if texto==reservadas[n]:
                  return False
              else:
                  n+=1
          return True

def isAssign():
    global i
    if es_id() and tokens[i+1]==":=":
          return True
    return False

def sentencias():
    global i
    if tokens[i]=="if":
          return seleccion()
    if tokens[i]=="while":
          return iteracion()
    if tokens[i]=="do":
          return repeticion()
    if tokens[i]=="cin":
          return sent_cin()
    if tokens[i]=="cout":
          return sent_cout()
    if tokens[i]=="{":
          return bloque()
    if isAssign():
          return asignacion()
    errorSintactico()

def seleccion():
    global i
    nombre="if"
    temp=Nodo(nombre)
    match("if")
    match('(')
    p=expresion()
    temp.agregar_hijos(p)
    match(')')      
    match("then")
    q=bloque()
    temp.agregar_hijos(q)
    if(tokens[i]=="else"):
        match("else")
        k=bloque()
        temp.agregar_hijos(k)
    return temp


def iteracion():
    global i
    nombre="while"
    temp=Nodo(nombre)
    match("while")      
    match('(')
    p=expresion()
    temp.agregar_hijos(p)
    match(')')
    q=bloque()
    temp.agregar_hijos(q)
    return temp

def repeticion():
    global i
    nombre="do"
    temp=Nodo(nombre)
    match("do")
    p=bloque()
    temp.agregar_hijos(p)
    match("until")
    match("(")
    q=expresion()
    temp.agregar_hijos(q)
    match(")")
    match(';')
    return temp

def bloque():
    global i
    match('{')
    temp=listaSentencias()
    match('}')
    return temp

#def expresion():
    #nombre=""      
    #if isCamparation():
          #nombre=str(tokens[i+1])
          #agregarElemento(arbol, expresion_simple(), nombre)
          #i+=1
          #match(nombre)
          #agregarElemento(arbol, expresion_simple(), nombre)
          #return nombre
    #else:
          #return exp_simple()
          
def expresion():
    global i
    nombre=""
    bandera=1
    temp=exp_simple()
    while tokens[i]=="<" or tokens[i]=="<=" or tokens[i]==">" or tokens[i]==">=" or tokens[i]=="==" or tokens[i]=="!=":
        bandera=0
        nombre=str(tokens[i])
        nuevo=Nodo(nombre)
        match(nombre)
        nuevo.agregar_hijos(temp)
        p=exp_simple()
        nuevo.agregar_hijos(p)
    if bandera==0:
        return nuevo
    else:
        return temp     


#def exp_simple():
    #nombre=""      
    #if isOps():
          #while tokens[i+1]=="+" or tokens[i+1]=="-":
              #nombre=str(tokens[i+1])
              #agregarElemento(arbol, termino(), nombre)
              #match(nombre)
              #agregarElemento(arbol, termino(), nombre)
              #return nombre   
   #else:
       #return termino()

def exp_simple():
    nombre=""
    global i
    bandera=1
    temp=termino()
    while tokens[i]=="+" or tokens[i]=="-":
        bandera=0
        nombre=str(tokens[i])
        nuevo=Nodo(nombre)
        match(nombre)
        nuevo.agregar_hijos(temp)
        p=termino()
        nuevo.agregar_hijos(p)
    if bandera==0:
        return nuevo
    else:
        return temp
    
def termino():
    nombre=""
    global i
    bandera=1
    temp=factor()
    while tokens[i]=="*" or tokens[i]=="/":
        bandera=0
        nombre=str(tokens[i])
        nuevo=Nodo(nombre)
        match(nombre)
        nuevo.agregar_hijos(temp)
        p=factor()
        nuevo.agregar_hijos(p)
    if bandera==0:
        return nuevo
    else:
        return temp
    
def factor():
    global i
    if tokens[i]=="(":
        match('(')
        temp=expresion()
        match(')')
        return temp 
    elif es_id():
        temp=Nodo(str(tokens[i]))
        i+=1
        return temp 
    else:
        try:
            if '.' in tokens[i]:
                #val = float(tokens[i])
                temp=Nodo(str(tokens[i]))
                i+=1
                return temp
            else:
                #val = int(tokens[i])
                temp=Nodo(str(tokens[i]))
                i+=1 
                return temp 
        except ValueError:
            errorSintactico()
         

    

def sent_cin():
    global i
    nombre="cin"
    temp=nombre(nombre)
    match("cin")
    if es_id():
        p=Nodo(str(tokens[i]))
        temp.agregar_hijos(p)
        i+=1
        match(';');
        return temp
    else:
        errorSintactico()

def sent_cout():
    global i
    nombre="cout"
    temp=Nodo(nombre)
    match("cout")
    p=expresion()
    temp.agregar_hijos(p)
    match(';');
    return temp

def asignacion():
    global i
    nombre=str(tokens[i+1])
    temp=Nodo(nombre)
    p=Nodo(str(tokens[i]))
    temp.agregar_hijos(p)
    i+=1
    match(nombre)
    q=expresion()
    temp.agregar_hijos(q)
    match(';')
    return temp


#archi=open("../../lexemas.txt",'r')
archi=open("lexemas.txt",'r')          
tokens=""
tokens = archi.read().splitlines()
programa()         
archi.close()
#sintactico.close()
