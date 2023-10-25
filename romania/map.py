import matplotlib.pyplot as plt
import networkx as nx
from romania import city, route_list

class point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

G = nx.Graph()
nodes = ['Arad', 'Bucarest', 'Craiova', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui','Zerind']

edges = [('Arad','Sibiu'), ('Arad','Timisoara'), ('Arad','Zerind'), ('Bucarest','Fagaras'), ('Bucarest','Giurgiu'), ('Bucarest','Pitesti'), ('Bucarest','Urziceni'), ('Craiova','Dobreta'), ('Craiova','Pitesti'), ('Craiova','Rimnicu'), ('Dobreta','Mehadia'), ('Eforie','Hirsova'), ('Fagaras','Sibiu'), ('Hirsova','Urziceni'), ('Iasi','Neamt'), ('Iasi','Vaslui'), ('Lugoj','Mehadia'), ('Lugoj','Timisoara'), ('Oradea','Sibiu'), ('Oradea','Zerind'), ('Pitesti','Rimnicu'), ('Rimnicu','Sibiu'), ('Urziceni','Vaslui')]

coords = {'Arad':(62,351), 'Bucarest':(520,107), 'Craiova':(302,46), 'Dobreta':(172,65), 'Eforie':(760,55), 'Fagaras':(382,290), 'Giurgiu':(484,23), 'Hirsova':(720,140), 'Iasi':(630,375), 'Lugoj':(172,184), 'Mehadia':(175,125), 'Neamt':(530, 429), 'Oradea':(122,470), 'Pitesti':(402,167), 'Rimnicu':(272,230), 'Sibiu':(235,300), 'Timisoara':(66,230), 'Urziceni':(606,141), 'Vaslui':(684,282),'Zerind':(88,410)}

G.add_nodes_from(nodes)
G.add_edges_from(edges)

def graph(city:city) -> None:
    nx.draw(G, pos=coords, node_color='gray', edge_color='black', with_labels='true') # Dibujamos todo el grafo

    nodes = route_list(city)
    edges_route = []
    for i in range(len(nodes) - 1):
        edges_route.append((nodes[i],nodes[i + 1]))
    GR = nx.Graph()
    GR.add_nodes_from(nodes[1:-2])
    GR.add_edges_from(edges_route)
    nx.draw(GR, pos=coords, node_color='cyan', edge_color='yellow', with_labels='true') # Dibujamos el recorrido
    GR = nx.Graph()
    GR.add_node(nodes[-1])
    nx.draw(GR, pos=coords, node_color='green', with_labels='true') # Dibujamos el origen
    GR = nx.Graph()
    GR.add_node(nodes[0])
    nx.draw(GR, pos=coords, node_color='red', with_labels='true') # Dibujamos el destino (Bucarest)

    plt.show()