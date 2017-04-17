from arbol import *
sintactico=open('sintactico.txt','w+')
i=0;
reservadas=("main","if","then","else","end","do","while","repeat","until","cin","cout","real","int","boolean")

def printElement(element):
    print("",element)
    
def match(expectedToken):
    if tokens[i]==excpectedToken:
        i+=1
    else:
        errorSintactico()

def errorSintactico():
    print("Syntax error en -> ",tokens[i])
    return; 
        
def programa():
    match("main")
    arbol=Arbol("main")
    match('{')
    if tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
        agregarElemento(arbol,listaDeclaracion(), "main")
    if tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
        agregarElemento(arbol,listaSentencias(), "main")
    match('})
          
def listaDeclaracion():
    nombre="lista-declaracion"
    agregarElemento(arbol, declaracion(), nombre)
    match(';')
    while tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
          agregarElemento(arbol, declaracion(), nombre)
          match(';')
    return nombre

def declaracion():
    nombre=""
    if tokens[i]=="int":
          match("int")
          nombre="int"
          agregarElemento(arbol, listaVariables(), nombre)
    if tokens[i]=="float":
          match("float")
          nombre="float"
          agregarElemento(arbol, listaVariables(), nombre)
    if tokens[i]=="boolean":
          match("boolean")
          nombre="boolean"
          agregarElemento(arbol, listaVariables(), nombre)
    return nombre

def listaVariables(tipo):
    nombre=str(tokens[i])
    if es_id():
          i+=1
          return nombre; 
    else:
          errorSintactico()     
          
          
def listaSentencias():
    nombre="lista-declaracion"
    agregarElemento(arbol, sentencias(), nombre)
    while tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
          agregarElemento(arbol, sentencias(), nombre)
    return nombre

def es_id():
    texto=tokens[i]
    j=0;
    n=0;
    if texto[j].isalpha():
          while n<len(reservadas)
              if texto==reservadas[n]
                  return false
          return true
    else:
          return false

def isAssign():
    if es_id() and tokens[i+1]==":=":
          return true
    return false

def sentencias():
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

    return errorSintactico()

def seleccion():
    nombre="if"
    match("if")
    match('(')
    agregarElemento(arbol, expresion(), nombre)
    match(')')      
    match("then")
    agregarElemento(arbol, bloque(), nombre)
    if(tokens[i]=="else"):
          match("else")
          agregarElemento(arbol, bloque(), nombre)
    return nombre


def iteracion():
    nombre="while"
    match("while")      
    match('(')      
    agregarElemento(arbol, expresion(), nombre)
    match(')')
    agregarElemento(arbol, bloque(), nombre)
    return nombre

def repeticion():
    nombre="do"
    match("do")
    agregarElemento(arbol, bloque(), nombre)
    match("while")
    match("(")
    agregarElemento(arbol, expresion(), nombre)
    match(")")
    match(';')
    return nombre

def bloque():
    match('{')
    return listaSentencias()
    match('}')

def expresion():
    nombre=""
    temp=exp_simple()
    while tokens[i]=="<" or tokens[i]=="<=" or tokens[i]==">" or tokens[i]==">=" or tokens[i]=="=" or tokens[i]=="!=":
          nombre=str(tokens[i])
          nuevo=Arbol(nombre)
          match(nombre)
          agregarElemento(nuevo, temp, nombre)
          agregarElemento(nuevo, exp_simple(), nombre)
          temp=nuevo
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
    temp=termino()
    while tokens[i]=="+" or tokens[i]=="-":
          nombre=str(tokens[i])
          nuevo=Arbol(nombre)
          match(nombre)
          agregarElemento(nuevo, temp, nombre)
          agregarElemento(nuevo, termino(), nombre)
          temp=nuevo
    return temp        
          
def termino():
    nombre=""
    temp=factor()
    while tokens[i]=="*" or tokens[i]=="/":
          nombre=str(tokens[i])
          nuevo=Arbol(nombre)
          match(nombre)
          agregarElemento(nuevo, temp, nombre)
          agregarElemento(nuevo, termino(), nombre)
          temp=nuevo
    return temp
          
def factor():      
    if tokens[i]=="(":
          match('(')
          temp=expresion()
          match(')')
    elif es_id():
          i+=1
          temp=Arbol(str(tokens[i-1]))
    else:
          try:
               val = float(tokens[i])
               i+=1
               temp=Arbol(str(tokens[i-1]))
         except ValueError:
               errorSintactico()
   return temp       

    

def sent_cin():
    match("cin")
    nombre="cin"
    if es_id():
          agregarElemento(arbol,tokens[i],nombre)
          i+=1
          return nombre
    else:
          errorSintactico()

def sent_cout():
    match("cout")
    nombre="cout"
    agregarElemento(arbol,expresion(),nombre)
    return nombre

def asignacion():
    nombre=str(tokens[i+1])
    agregarElemento(arbol,tokens[i],nombre)
    i+=1
    match(nombre)
    agregarElemento(arbol,expresion(),nombre)
    return nombre


archi=open("../../lexemas.txt",'r')
tokens=""
tokens = archi.read().splitlines()
programa()
archi.close()
sintactico.close()
