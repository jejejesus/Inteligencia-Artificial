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

def expand(ciudad) -> dict[str, int]:
    return routes[ciudad]

print(expand("Iasi"))