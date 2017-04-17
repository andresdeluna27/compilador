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

def listaVariables():
    nombre=""
    if tokens[i].isalpha():
          

def listaSentencias():
    nombre="lista-declaracion"
    agregarElemento(arbol, sentencias(), nombre)
    return nombre

def declaracion():
    nombre=lexema[i]
    agregarElemento(arbol, identificador(), nombre)

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
    if es_id() && tokens[i+1]==":=":
          return true
    return false
archi=open("../../lexemas.txt",'r')
tokens=""
tokens = archi.read().splitlines()
programa()
archi.close()
sintactico.close()
