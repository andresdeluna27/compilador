class Nodo(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []
        self.hermano = None
        self.padre = None

    def agregar_hijos(self, obj):
        self.hijos.append(obj)

    def agregar_hermano(self, obj):
        self.hermano = obj

    def agregar_hermano(self, obj):
        self.hermano = obj    
        
    def imprimir_nombres(self):
        for hijo in self.hijos:
            print(str(hijo.nombre))

    def getName(self):
        return str(self.nombre)
            
def recorrer_arbol(arbol, ite):
    if arbol!=None:
        for i in range(ite):
            print("-", end="")
        print(" ",arbol.getName())
        
        if len(arbol.hijos)!=0:
            ite+=1
            for hijo in arbol.hijos:
                recorrer_arbol(hijo, ite)
        if arbol.hermano!=None:
            ite-=1
            recorrer_arbol(arbol.hermano, ite)
        
