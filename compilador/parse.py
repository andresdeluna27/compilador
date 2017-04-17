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
    match('{')
    agregarElemento(arbol,"main", "programa")
    agregarElemento(arbol,listaDeclaracion(), "programa")
    agregarElemento(arbol,listaSentencias(), "programa")
    match('})
          
def listaDeclaracion():
    nombre="lista-declaracion"
    if tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
          agregarElemento(arbol, declaracion(), nombre)
    return nombre
          
archi=open("../../lexemas.txt",'r')
tokens=""
tokens = archi.read().splitlines()
if tokens[i]=="main":
    arbol = Arbol("programa")
    i+=1
    programa()
else:
    errorSintactico()
archi.close()
sintactico.close()
