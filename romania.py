routes = {
    'Arad': {'Zerind': 75,'Sibiu': 140,'Timisoara': 118},
    'Bucarest': {'Giurgiu': 90, 'Urziceni': 85, 'Pitesti': 101,'Fagaras': 211},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu': 146},
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
    'Pitesti': {'Rimnicu': 97, 'Bucarest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80,'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99,'Arad': 140, 'Oradea': 151},
    'Timisoara': { 'Lugoj': 111, 'Arad': 118,},
    'Urziceni': {'Bucarest': 85,'Hirsova': 98,'Vaslui': 142,},             
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': { 'Oradea': 71,'Arad': 75},                      
}

lineal_distance = {
    'Arad': 266,
    'Bucarest': 0,
    'Craiova': 160,
    'Dovreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244, 
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

class city:
    city_name:str = ""
    distance_traveled:int = 0

    def __init__(self, city_name:str, previous_city = None, distance_traveled:int = 0) -> None:
        self.city_name = city_name
        self.previous_city = previous_city
        self.distance_traveled = distance_traveled

    def goal_test(self) -> bool:
        return self.city_name == "Bucarest"
    
    def expand(self) -> list:
        off_springs:list[city] = []
        for off_spring in routes[self.city_name]:
            new_distance:int = self.distance_traveled + routes[self.city_name][off_spring]
            off_springs.append(city(city_name=off_spring, previous_city=self, distance_traveled=new_distance))
        return off_springs
    
    def heuristic(self) -> int:
        return self.distance_traveled + lineal_distance[self.city_name]

    def __repr__(self) -> str:
        return f"City: {self.city_name:10}, Traveled distance: {str(self.distance_traveled):>5}, Heuristic: {str(self.heuristic()):>5}{f', Previous city: {self.previous_city.city_name}' if self.previous_city != None else ''}"
    
def route(end_city:city, route_str:str = "") -> str:
    route_str = (end_city.city_name + "(" + str(end_city.distance_traveled) + ") -> ") + route_str
    if end_city.previous_city != None: return route(end_city.previous_city, route_str)
    else: return route_str[0:-4]

def a_star_search(frontier:list[city]) -> str:
    if frontier == []:
        return "Solution not found", None
    current_city = frontier.pop(0)
    print(current_city)
    if current_city.goal_test():
        return "Solution found", current_city
    off_springs = current_city.expand()
    frontier += off_springs
    frontier.sort(key=city.heuristic)

    return a_star_search(frontier)        

def main():
    initial_city = city("Neamt")
    frontier:list[city] = []
    frontier.append(initial_city)
    message, goal = a_star_search(frontier)
    print("\n" + message + ": " + route(goal) + "\n")

if __name__ == "__main__":
    main()