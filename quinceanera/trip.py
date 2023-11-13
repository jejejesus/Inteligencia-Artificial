from itertools import permutations
from tables import routes_cities
from tables import coor
import requests
import polyline
import folium
from folium.plugins import MarkerCluster
from folium import Icon

origin_city = ""
        
def all_permutations(origin_city:str, cities:list[str]) -> list[list[str]]: # Función que recibe una lista de ciudades y retorna todas sus posibles permutaciones
    permutations_return:list[list[str]] = []
    for permutation in list(permutations(cities)):
        permutations_return.append([origin_city] + list(permutation) + [origin_city])
    return permutations_return

def evaluate_permutation(cities:list[str]) -> int: # Función que calcula el costo de una permutación, utilizando la tabla de costos A*
    if len(cities) <= 2: return 0
    final_cost = 0
    for city in cities:
        next_city = cities[cities.index(city) + 1]
        for route in routes_cities:
            if (route[1] == city and route[-1] == next_city) or (route[-1] == city and route[1] == next_city):
                final_cost += route[0]
                break
    return final_cost

def shortest_trip(origin_city:str, cities:list[str]) -> (list[str], int):
    permutations_aux = all_permutations(origin_city, cities)
    permutations_aux.sort(key=evaluate_permutation)
    return permutations_aux[0], evaluate_permutation(permutations_aux[0])

def route_str(cities:list[str]) -> str:
    route = ""
    waypoint_city = []
    for city in cities:
        if(city == cities[0]):
            origin_map = coor[city]
        else:
            waypoint_city.append(city)
        route += city + " -> "

    waypoint_coor = []
    
    for ciudad in waypoint_city:
        if ciudad in coor:
            waypoint_coor.append(str(coor[ciudad]))

    waypoints_str = "|".join(f"{coord}" for coord in waypoint_coor)

    # Ingresa tu clave de API de Google Maps aquí
    API_KEY = "AIzaSyCqnAQOreRe9SEwRWS_V_wmZHh7mV0YxoA"

    # URL de la API de Google Maps
    URL = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
    "origin": origin_map,
    "destination": origin_map,
    "waypoints": waypoints_str,  # Agrega más destinos aquí
    "optimize": "true",  # Intenta optimizar el orden de los waypoints
    "key": API_KEY,
    }

    # Realiza la solicitud HTTP
    response = requests.get(URL, params=params)

    # Procesa la respuesta
    if response.status_code == 200:
        # La solicitud se realizó correctamente
        directions = response.json()

        # Verificar si hay rutas disponibles
        if "routes" in directions and directions["routes"]:
            # Obtener la polilínea de la respuesta
            polyline_str = directions["routes"][0]["overview_polyline"]["points"]

            # Decodificar la polilínea para obtener las coordenadas de la ruta
            coordinates = polyline.decode(polyline_str)

            # Crear un objeto de mapa folium centrado en el origen
            m = folium.Map(location=(origin_map[0], origin_map[1]), zoom_start=8)

            folium.Marker(location=(float(origin_map.split(',')[0]), float(origin_map.split(',')[1])), popup="Inicio", icon=folium.Icon(color='green')).add_to(m)

            # Trazar la ruta en el mapa
            folium.PolyLine(locations=coordinates, color='blue').add_to(m)

            # Agregar marcadores con íconos personalizados
            marker_cluster = MarkerCluster().add_to(m)
            for i, coord in enumerate(waypoint_coor):
                lat, lon = map(float, coord.split(','))
                icon = Icon(color="red", prefix="fa", icon="circle")  # Puedes cambiar el ícono aquí
                folium.Marker(location=[lat, lon], popup=f"Marcador #{i+1} - Coordenadas: {lat}, {lon}", icon=icon).add_to(marker_cluster)

            # Guardar el mapa en un archivo HTML
            m.save("directions_map_folium_with_custom_markers.html")
            print("Mapa guardado como 'directions_map_folium_with_custom_markers.html'")

    else:
        # La solicitud no se realizó correctamente
        print(response.status_code)


    return route[0:-4].upper()
