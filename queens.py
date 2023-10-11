
def attack(v:list[int]) -> int: # Función que retorna el número de ataques en un tablero
    n = len(v)
    A = 0
    for i in range(n):
        for j in range(i + 1, n):
            if v[i] == v[j]:
                A += 2
            if abs(i - j) == abs(v[i] - v[j]):
                A += 2
    
    return A

def goal_test(v:list[int]) -> bool: # Función que retorna si el estado actual es el objetivo
    return attack(v) == 0

def expand(v:list[int]) -> list[int] # Función para obtener

def dls(frontier:list[int], limit:int): # Método de busqueda Depth-Limited Search
    current_state = frontier[0]

    if goal_test(current_state):
        return "Solución encontrada"
    
    if current_level > limit:
        print()
    
