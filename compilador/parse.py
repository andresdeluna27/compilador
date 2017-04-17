from arbol import *
sintactico=open('sintactico.txt','w+')
i=0;

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
    match('{')
    if tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
        agregarElemento(arbol,listaDeclaracion(), "main")
    agregarElemento(arbol,listaSentencias(), "main")
    match('})
          
def listaDeclaracion():
    nombre="lista-declaracion"
    agregarElemento(arbol, declaracion(), nombre)
    return nombre

def listaSentencias():
    nombre="lista-declaracion"
    agregarElemento(arbol, sentencias(), nombre)
    return nombre      
          
archi=open("../../lexemas.txt",'r')
tokens=""
tokens = archi.read().splitlines()
programa()
archi.close()
sintactico.close()
