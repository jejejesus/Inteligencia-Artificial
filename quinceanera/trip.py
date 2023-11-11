from itertools import permutations

origin_city = "Paris"

class city: # Clase City

    def __init__(self, city_name:str, previous_city = None, cities_traveled:int = 1, distance_traveled:int = 0) -> None:
        self.city_name = city_name
        self.previous_city = previous_city
        self.cities_traveled = cities_traveled
        self.distance_traveled = distance_traveled

    def goal_test(self) -> bool: # Función Goal Test para saber si estamos en la ciudad en la que empezamos y ya recorrimos 8 ciudades
        return self.city_name == origin_city and self.cities_traveled == 9
    
    def expand(self) -> list: # Función Expand, en esta también se calcula la distancia total viaja de cada off spring
        off_springs:list[city] = []
        #visited = visited_list(self)
        for off_spring in routes[self.city_name]: # Por cada ruta que tenga la ciudad...
            #if off_spring not in visited:
            new_distance:int = self.distance_traveled + routes[self.city_name][off_spring] # Calculamos la nueva distancia recorrida a cada offspring
            off_springs.append(city(city_name=off_spring, previous_city=self, cities_traveled=self.cities_traveled + 1, distance_traveled=new_distance)) # Agregamos al offspring a la lista de offsprings
        return off_springs
    
    def heuristic(self) -> int: # Función para calcular la herística
        return self.distance_traveled + lineal_distance[origin_city][self.city_name]

    def __repr__(self) -> str:
        return f"City: {self.city_name:10}, Traveled distance: {str(self.distance_traveled):>5}, Heuristic: {str(self.heuristic()):>5}, Cities traveled: {str(self.cities_traveled):>3}{f', Previous city: {self.previous_city.city_name}' if self.previous_city != None else ''}"

def route_str(end_city:city, route:str = "") -> str: # Función que recibe una ciudad y retorna un string con la ruta que se tomó para llegar a ella
    route = (end_city.city_name + "(" + str(end_city.distance_traveled) + ") -> ") + route
    if end_city.previous_city != None:
        return route_str(end_city.previous_city, route)
    else:
        return route[0:-4]

def visited_list(end_city:city, route:list[str] = []) -> list[str]: # Función que recibe una ciudad y retorna un lista con la ruta que se tomó para llegar a ella        
        if end_city.city_name not in route: route.append(end_city.city_name)
        if end_city.previous_city != None:
            return visited_list(end_city.previous_city, route)
        else:
            return route[1:]
        
def all_permutations(cities:list[str]) -> list[list[str]]: # Función que recibe una lista de ciudades y retorna todas sus posibles permutaciones
    return list(permutations(cities))

def all_permutations_str(permutations:list[list[str]]): # Función que imprime todas las permutaciones generadas
    for permutation in permutations:
        print(permutation)

def a_star_search(frontier:list[city]) -> tuple[str, city]: # Función de búsqueda A*
    if frontier == []: # Verificamos si frontier está vacío
        return "Solution not found", None
    current_city = frontier.pop(0) # Sacamos el primer elemento
    print(current_city)
    if current_city.goal_test(): # Verificamos si la ciudad actual es la meta
        return "Solution found", current_city
    if current_city.cities_traveled > 8:
        return "Limit reached", None
    off_springs = current_city.expand() # Obtenemos los offsprings de la ciudad actual
    frontier += off_springs # Agregamos los offsprings a frontier
    frontier.sort(key=city.heuristic) # Ordenamos frontier según la heurística

    return a_star_search(frontier)

possibilities = all_permutations(["Andorra", "Madrid", "Paris", "Lisbon"])
all_permutations_str(possibilities)