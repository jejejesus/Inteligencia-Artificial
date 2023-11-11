from itertools import permutations
from tables import routes_cities

origin_city = ""
        
def all_permutations(cities:list[str]) -> list[list[str]]: # Función que recibe una lista de ciudades y retorna todas sus posibles permutaciones
    origin_city:str = cities.pop(0)
    permutations_return:list[list[str]] = []
    for permutation in list(permutations(cities)):
        permutations_return.append([origin_city] + list(permutation) + [origin_city])
    return permutations_return

def evaluate_permutation(cities:list[str]) -> int: # Función que calcula el costo de una permutación, utilizando la tabla de costos A*
    final_cost = 0
    for city in cities[0:-1]:
        next_city = cities[cities.index(city) + 1]
        for route in routes_cities:
            if (route[1] == city and route[-1] == next_city) or (route[-1] == city and route[1] == next_city):
                final_cost += route[0]

    return final_cost

def shortest_trip(origin_city:str, cities:list[str]) -> list[str]:
    permutations = all_permutations([origin_city] + cities)
    permutations.sort(key=evaluate_permutation)
    return permutations[0]


'''
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
'''