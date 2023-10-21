import random
import sys
sys.setrecursionlimit(10000)

class board():

    level = 0
    queens = []
    visited:list[list[int]] = []

    def __init__(self, level:int = 0, size:int = 4, queens:list[int] = []) -> None:
        self.level = level
        self.size = size
        if queens == []:
            self.queens = [0] * size
        else:
            self.queens = queens
        self.visited.append(self.queens)
            

    def attacks(self) -> int: # Función que retorna el número de ataques en un tablero
        n = len(self.queens)
        A = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.queens[i] == self.queens[j]:
                    A += 2
                if abs(i - j) == abs(self.queens[i] - self.queens[j]):
                    A += 2
        return A

    def goal_test(self) -> bool: # Función que retorna si el estado actual es el objetivo
        return self.attacks() == 0
    
    def expand(self) -> list: # Función para obtener
        expanded:list[board] = []
        aux:list[int] = []
        for i in range(self.size):
            aux = []
            aux += self.queens
            if aux[i] + 1 < self.size:
                aux[i] += 1  
            else:
                num = random.randint(0, self.size - 1)
                aux[i] -= num
            if not(self.visited.__contains__(aux)):
                expanded.append(board(self.level + 1, self.size, aux))
                self.visited.append(aux)  
        return expanded
    
    def __repr__(self) -> str:
        return "state: " + str(self.queens) + ", attacks: " + str(self.attacks()) + ", level: " + str(self.level)
    
def bf_s(frontier:list[board]) -> tuple[str, board]: #Función de búsqueda Breadth-First Search
    if frontier == []:
        return "Solution not found or does not exist", None
    current_state:board = frontier.pop(0)
    print(current_state)
    if current_state.goal_test():
        return "Solution found: " + str(current_state), current_state
    off_springs = current_state.expand()
    frontier = frontier + off_springs

    return bf_s(frontier)

def df_s(frontier:list[board]) -> tuple[str, board]: #Función de búsqueda Depth-First Search
    if frontier == []:
        return "Solution not found or does not exist", None
    current_state:board = frontier.pop(0)
    print(current_state)
    if current_state.goal_test():
        return "Solution found: " + str(current_state), current_state
    off_springs = current_state.expand()
    frontier = off_springs + frontier

    return df_s(frontier)


def dl_s(frontier:list[board], limit:int) -> tuple[str, board]: # Función de búsqueda Depth-Limited Search
    if frontier == []:
        return "Solution not found or does not exist", None
    current_state:board = frontier.pop(0)
    current_level = current_state.level
    print(current_state)
    if current_state.goal_test():
        return "Solution found: " + str(current_state), current_state
    if current_level >= limit:
        return "Limit reached", None
    off_springs = current_state.expand()
    frontier = off_springs + frontier

    return dl_s(frontier, limit)

def idl_s(frontier:list[board], limit:int) -> tuple[str, board]: # Función de búsqueda Iterated Depth-Limited Search
    while True:
        print(dl_s(frontier, limit))
        limit += 2

def g_s(frontier:list[board]) -> tuple[str, board]: # Función de búsqueda Greedy Search
    if frontier == []:
        return "Solution not found or does not exist", None
    current_state:board = frontier.pop(0)
    print(current_state)
    if current_state.goal_test():
        return "Solution found: " + str(current_state), current_state
    off_springs = current_state.expand()
    off_springs.sort(key=board.attacks)
    if off_springs == []:
        return "Solution not found or does not exist", None
    
    return g_s([off_springs[0]])