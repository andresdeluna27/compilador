from arbol import *
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
    global arbol
    nombre="main"
    arbol=Arbol(nombre)
    match("main")
    match('{')
    if tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
        agregarElemento(arbol,listaDeclaracion(),nombre)
    if tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
        agregarElemento(arbol,listaSentencias(), nombre)
    match('}')
          
def listaDeclaracion():
    global i
    global arbol
    nombre="lista-declaracion"
    temp=Arbol(nombre)
    agregarElemento(temp, declaracion(), nombre)
    match(';')
    while tokens[i]=="int" or tokens[i]=="float" or tokens[i]=="boolean":
          agregarElemento(temp, declaracion(), nombre)
          match(';')
    return temp

def declaracion():
    nombre=""
    global i
    global arbol
    if tokens[i]=="int":
          match("int")
          nombre="int"
          temp=Arbol(nombre)
          agregarElemento(temp, listaVariables(nombre), nombre)
    if tokens[i]=="float":
          match("float")
          nombre="float"
          temp=Arbol(nombre)
          agregarElemento(temp, listaVariables(nombre), nombre)
    if tokens[i]=="boolean":
          match("boolean")
          nombre="boolean"
          temp=Arbol(nombre)
          agregarElemento(temp, listaVariables(nombre), nombre)
    return temp

def listaVariables(tipo):
    global i
    global arbol
    if es_id():
          nombre=str(tokens[i])
          i+=1
          temp=Arbol(tipo)
          agregarElemento(temp, nombre, tipo)
          match(',')
          while tokens[i]!=';':
              if es_id():
                  hermano=str(tokens[i])
                  i+=1
                  agregarElemento(temp, hermano, tipo)
                  if tokens[i]!=';':
                      match(',')        
          return temp; 
    else:
          errorSintactico()     
          
          
def listaSentencias():
    global i
    nombre="lista-sentencias"
    temp=Arbol(nombre)
    agregarElemento(temp, sentencias(), nombre)
    while tokens[i]=="if" or tokens[i]=="while" or tokens[i]=="do" or tokens[i]=="cin" or tokens[i]=="cout" or isAssign():
          agregarElemento(temp, sentencias(), nombre)
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
    temp=Arbol(nombre)
    match("if")
    match('(')
    agregarElemento(temp, expresion(), nombre)
    match(')')      
    match("then")
    agregarElemento(temp, bloque(), nombre)
    if(tokens[i]=="else"):
          match("else")
          agregarElemento(temp, bloque(), nombre)
    return temp


def iteracion():
    global i
    global arbol
    nombre="while"
    temp=Arbol(nombre)
    match("while")      
    match('(')      
    agregarElemento(temp, expresion(), nombre)
    match(')')
    agregarElemento(temp, bloque(), nombre)
    return temp

def repeticion():
    global i
    global arbol
    nombre="do"
    temp=Arbol(nombre)
    match("do")
    agregarElemento(temp, bloque(), nombre)
    match("until")
    match("(")
    agregarElemento(temp, expresion(), nombre)
    match(")")
    match(';')
    return temp

def bloque():
    global i
    match('{')
    nombre=listaSentencias()
    match('}')
    return nombre

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
    global arbol
    nombre=""
    temp=exp_simple()
    while tokens[i]=="<" or tokens[i]=="<=" or tokens[i]==">" or tokens[i]==">=" or tokens[i]=="==" or tokens[i]=="!=":
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
    global i
    global arbol
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
    global i
    global arbol
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
    global i
    global arbol
    if tokens[i]=="(":
          match('(')
          temp=expresion()
          match(')')
          return temp 
    elif es_id():
          i+=1
          temp=Arbol(str(tokens[i-1]))
          return temp 
    else:
          try:
               val = float(tokens[i])
               temp=Arbol(str(tokens[i]))
               i+=1
               return temp 
          except ValueError:
               errorSintactico()
         

    

def sent_cin():
    global i
    global arbol
    match("cin")
    nombre="cin"
    temp=Arbol(nombre)
    if es_id():
          agregarElemento(temp,tokens[i],nombre)
          i+=1
          match(';');
          return temp
    else:
          errorSintactico()

def sent_cout():
    global i
    match("cout")
    nombre="cout"
    temp=Arbol(nombre)
    agregarElemento(temp,expresion(),nombre)
    match(';');
    return temp

def asignacion():
    global i
    nombre=str(tokens[i+1])
    temp=Arbol(nombre)
    agregarElemento(temp,tokens[i],nombre)
    i+=1
    match(nombre)
    agregarElemento(temp,expresion(),nombre)
    match(';')
    return temp


#archi=open("../../lexemas.txt",'r')
archi=open("lexemas.txt",'r')          
tokens=""
tokens = archi.read().splitlines()
programa()
ejecutarAnchoPrimero(arbol, printElement)          
archi.close()
#sintactico.close()
