from nutree import Tree, Node

arbol = Tree("Rutas") # Se crea el árbol y sus nodos
n1 = arbol.add(1)
n2 = n1.add(2)
n3 = n2.add(4)
n4 = n3.add(8)
n4 = n3.add(9)
n3 = n2.add(5)
n4 = n3.add(10)
n4 = n3.add(11)
n5 = n4.add(16)
n2 = n1.add(3)
n3 = n2.add(6)
n4 = n3.add(12)
n4 = n3.add(13)
n5 = n4.add(17)
n3 = n2.add(7)
n4 = n3.add(14)
n4 = n3.add(15)

arbol.print()
print()

EI = arbol.find(1) # Estado inicial
EO = arbol.find(10) # Estado objetivo
F = [EI]

def BFS(F:list[Node]): # Función de búsqueda - Broad First Search
    if F == []:
        print("F está vacía")
        return
    EA:Node = F.pop(0)
    if estado_Objetivo(EA):
        print(f"El estado actual \"{EA}\" es la meta")
        return
    OF = EA.children
    F = F + OF
    print(f"EA: {EA.data} \t F: {listar_Nodos(F)}")
    BFS(F)

def estado_Objetivo(EA) -> bool: # Función para validar si el estado es el objetivo
    return EA == EO

def listar_Nodos(F:list[Node]) -> str: # Función para listar los valores en una cadena
    lista = ""
    for nodo in F:
        lista += nodo.name + ", "
    return lista[0:-2]

BFS(F) # Llamamos a la función de búsqueda
print()