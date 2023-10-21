routes = [[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None, 140, 118,None,None,  75],
          [None,None,None,None,None, 211,  90,None,None,None,None,None,None, 101,None,None,None,  85,None,None],
          [None,None,None, 120,None,None,None,None,None,None,None,None,None, 138, 146,None,None,None,None,None],
          [None,None, 120,None,None,None,None,None,None,None,  75,None,None,None,None,None,None,None,None,None],
          [None,None,None,None,None,None,None,  86,None,None,None,None,None,None,None,None,None,None,None,None],
          [None, 211,None,None,None,None,None,None,None,None,None,None,None,None,None,  99,None,None,None,None],
          [None,  90,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
          [None,None,None,None,  86,None,None,None,None,None,None,None,None,None,None,None,None,  98,None,None],
          [None,None,None,None,None,None,None,None,None,None,None,  87,None,None,None,None,None,None,  92,None],
          [None,None,None,None,None,None,None,None,None,None,  70,None,None,None,None,None, 111,None,None,None],
          [None,None,None,  75,None,None,None,None,None,  70,None,None,None,None,None,None,None,None,None,None],
          [None,None,None,None,None,None,None,None,  87,None,None,None,None,None,None,None,None,None,None,None],
          [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None, 151,None,None,None,  71],
          [None, 101, 138,None,None,None,None,None,None,None,None,None,None,None,  97,None,None,None,None,None],
          [None,None, 146,None,None,None,None,None,None,None,None,None,None,  97,None,  80,None,None,None,None],
          [ 140,None,None,None,None,  99,None,None,None,None,None,None, 151,None,  80,None,None,None,None,None],
          [ 118,None,None,None,None,None,None,None,None, 111,None,None,None,None,None,None,None,None,None,None],
          [None,  85,None,None,None,None,None,  98,None,None,None,None,None,None,None,None,None,None, 142,None],
          [None,None,None,None,None,None,None,None,  92,None,None,None,None,None,None,None,None, 142,None,None],
          [  75,None,None,None,None,None,None,None,None,None,None,None,  71,None,None,None,None,None,None,None]]
    
lineal_distance = {
    "Arad": 266,
    "Bucarest": 0,
    "Craiova": 160,
    "Dovreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

class to_bucarest:
    frontier:list[str] = []
    traveled_distance:int = 0

    def __init__(self, actual_state:str) -> None:
        self.frontier.append(actual_state)

    def goal_test(state:str) -> bool:
        return state == "Bucarest"
    
    """
        TO DO
    def expand() -> list:
        state = frontier[-1]
        off_springs = []
        for routes in 
        return
    """
        
    def a_star_search(self):
        if self.frontier == []:
            return "Solution not found or does not exist"
        actual_state = self.frontier.pop(0)
        if self.goal_test(actual_state):
            return "Solution found: " + str(self)
        # off_springs = self.expand() TO DO
        # off_springs
        
        
    def __repr__(self) -> str:
        ruta:str = ""
        for state in self.frontier:
            ruta += state + " -> "
        return ruta[0:-4] + ", Total: " + str(self.traveled_distance)
        
