from collections import deque

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento
        self.valor = 0; 

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))


def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        encontrado = buscarSubarbol(subarbol, elemento)
        if encontrado != None:
            return encontrado
    return None   # Exceptions

def profundidad(arbol):
    if len(arbol.hijos) == 0:
        return 1
    profundidades = map(profundidad, arbol.hijos)
    return 1 + max(profundidades) 

def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])


#
# RECORRIDOS
#

def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)

def ejecutarAnchoPrimero(arbol, funcion, cola = deque()):
    funcion(arbol.elemento)
    if (len(arbol.hijos) > 0):
        cola.extend(arbol.hijos)
    if (len(cola) != 0):
        ejecutarAnchoPrimero(cola.popleft(), funcion, cola)                                               
