class board():

    level = 0
    queens = []

    def __init__(self, level:int = 0, size:int = 4, queens:list[int] = []) -> None:
        self.level = level
        self.size = size
        if queens == []:
            for i in range(size):
                self.queens.append(1)
        else:
            self.queens = queens
            

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
                expanded.append(board(self.level + 1, self.size, aux))
            else:
                next          
        return expanded
    
    def __repr__(self) -> str:
        return "state: " + str(self.queens) + ", level: " + str(self.level)
    


def dls(frontier:list[board], limit:int) -> str: # Función de busqueda Depth-Limited Search
    if frontier == []:
        return "Solution not found or does not exist"
    current_state:board = frontier.pop(0)
    current_level = current_state.level
    print(current_state)
    if current_state.goal_test():
        return "Solution found: " + str(current_state)
    if current_level >= limit:
        return "Limit reached"
    off_springs = current_state.expand()
    frontier = off_springs + frontier

    return dls(frontier, limit)