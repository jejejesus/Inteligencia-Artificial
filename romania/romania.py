routes = {
    'Arad': {'Zerind': 75,'Sibiu': 140,'Timisoara': 118},
    'Bucarest': {'Giurgiu': 90, 'Urziceni': 85, 'Pitesti': 101,'Fagaras': 211},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Dovreta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Giurgiu': {'Bucarest': 90},
    'Hirsova': { 'Eforie': 86,'Urziceni': 98},
    'Iasi': { 'Neamt': 87, 'Vaslui': 92},
    'Lugoj': { 'Mehadia': 70,'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucarest': 101, 'Craiova': 138},
    'Rimnicu Vilcea': {'Sibiu': 80,'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu Vilcea': 80, 'Fagaras': 99,'Arad': 140, 'Oradea': 151},
    'Timisoara': { 'Lugoj': 111, 'Arad': 118,},
    'Urziceni': {'Bucarest': 85,'Hirsova': 98,'Vaslui': 142,},             
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': { 'Oradea': 71,'Arad': 75},                      
}

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


traveled_distance:int = 0

class to_bucarest:
    
    def goal_test() -> bool:
        for key in frontier[-1]:
            return key == "Bucarest"

    def expand() -> dict[str, int]:
        
        return routes[frontier[-1]]
    
    def f(off_spring:dict[str, int]) -> int:
        for key in off_spring: 
            return (traveled_distance + off_spring[key]) + lineal_distance[key]
    
    def a_star_search(frontier:list[str]) -> str:
        if frontier == []:
            return "Solution not found or does not exist"
        actual_state = frontier.pop(0)
        if actual_state.goal_test():
            return "Solution found: " + str(actual_state)
        off_springs = actual_state.expand()
        frontier += off_springs
        frontier.sort(key=to_bucarest.f)

        return a_star_search(frontier)
        
'''
    def __repr__(self) -> str:
        ruta:str = ""
        for state in self.frontier:
            ruta += state + " -> "
        return ruta[0:-4] + ", Total: " + str(self.traveled_distance)
'''        