from romania import city, a_star_search, route_str, lineal_distance
from map import graph

def main(): # Método main
    print("\n== ROMANIA ==" + 
        "\n\nCities:" +
        "\n  - Arad      - Mehadia" + 
        "\n  - Bucarest  - Neamt" + 
        "\n  - Craiovia  - Oradea" + 
        "\n  - Dobreta   - Pitesti" + 
        "\n  - Eforie    - Rimnicu " + 
        "\n  - Fagaras   - Sibiu" + 
        "\n  - Giurgiu   - Timisoara" + 
        "\n  - Hirsova   - Urziceni" + 
        "\n  - Iasi      - Vaslui" + 
        "\n  - Lugoj     - Zerind")
    
    flag = True
    while flag:
        try:
            origin = str(input(" Choose origin city: "))
        except:
            flag = True
        if origin in lineal_distance:
            flag = False

    initial_city = city(origin) # Se declara la ciudad inicial
    frontier:list[city] = []
    frontier.append(initial_city) # Se agrega a la frontera
    message, goal = a_star_search(frontier) # Llamanos a la función de búsqueda y recibimos un mensaje y la ciudad destino con la ruta recorrida
    print("\n" + message + ": " + route_str(goal) + "\n")
    graph(goal)

if __name__ == "__main__":
    main()