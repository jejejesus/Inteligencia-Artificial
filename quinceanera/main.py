from trip import origin_city, city, route_str, a_star_search

def main(): # Método main

    print("Origin city: " + origin_city)

    initial_city = city(origin_city) # Se declara la ciudad inicial
    frontier:list[city] = []
    frontier.append(initial_city) # Se agrega a la frontera
    message, goal = a_star_search(frontier) # Llamanos a la función de búsqueda y recibimos un mensaje y la ciudad destino con la ruta recorrida
    print("\n" + message + (": " + route_str(goal) if goal != None else "") + "\n")

if __name__ == "__main__":
    main()