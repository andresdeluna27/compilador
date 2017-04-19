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

    def recorrer_arbol(self):
        print(str(self.nombre))
        for hermano in self.hermanos:
            recorrer_arbol(hermano)
        for hijo in self.hijos:
            recorrer_arbol(hijo)
            
def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(str(arbol.nombre))
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)
        

        
