import tkinter as tk
from itertools import permutations
from random import randrange
from tkinter import ttk, DISABLED, NORMAL, messagebox

routes = {
    'Amsterdam': {'Berlin': 657, 'Brussels': 210, 'Vienna': 1145},
    'Andorra': {'Bern': 1044, 'Madrid': 619, 'Paris': 864, 'Rome': 1385},
    'Berlin': {'Amsterdam': 657,'Bern': 956, 'Brussels': 868, 'Luxembourg': 763, 'Rome': 1503, 'Vienna': 681, 'Warsaw': 574},
    'Bern': {'Andorra': 1044, 'Berlin': 957, 'Luxembourg': 447, 'Paris': 564, 'Rome': 851, 'Vienna': 944, 'Warsaw': 1444},
    'Brussels': {'Amsterdam': 210, 'Berlin': 868, 'Luxembourg': 224, 'Paris': 312},
    'Lisbon': {'Madrid': 633},
    'Luxembourg': {'Amsterdam': 391, 'Berlin': 763, 'Bern': 447, 'Brussels': 224, 'Paris': 373, 'Vienna': 939},
    'Madrid': {'Andorra': 619, 'Lisbon': 633, 'Paris': 1275},
    'Paris': {'Andorra': 864, 'Bern': 564, 'Brussels': 312, 'Luxembourg': 373, 'Madrid': 1275},
    'Rome': {'Andorra': 1385, 'Bern': 851, 'Vienna': 1122},
    'Vienna': {'Amsterdam': 1145, 'Berlin': 681, 'Bern': 944, 'Luxembourg': 939, 'Rome': 1122, 'Warsaw': 727},
    'Warsaw': {'Berlin': 574, 'Bern': 1444, 'Vienna': 727}              
}
# Tabla de distancias lineales a Bucarest
lineal_distance = {
    'Amsterdam': {'Amsterdam': 0, 'Andorra': 1125, 'Berlin': 578, 'Bern': 630, 'Brussels': 173, 'Lisbon': 1865, 'Luxembourg': 319, 'Madrid': 1481, 'Paris': 430, 'Rome': 1296, 'Vienna': 937, 'Warsaw': 1096},
    'Andorra': {'Amsterdam': 1125, 'Andorra': 0, 'Berlin': 1424, 'Bern': 680, 'Brussels': 952, 'Lisbon': 994, 'Luxembourg': 865, 'Madrid': 494, 'Paris': 709, 'Rome': 908, 'Vienna': 1321, 'Warsaw': 1816},
    'Berlin': {'Amsterdam': 578, 'Andorra': 1424, 'Berlin': 0, 'Bern': 753, 'Brussels': 652, 'Lisbon': 2316, 'Luxembourg': 604, 'Madrid': 1871, 'Paris': 880, 'Rome': 1181, 'Vienna': 522, 'Warsaw': 517},
    'Bern': {'Amsterdam': 630, 'Andorra': 680, 'Berlin': 753, 'Bern': 0, 'Brussels': 489, 'Lisbon': 1627, 'Luxembourg': 375, 'Madrid': 1152, 'Paris': 435, 'Rome': 689, 'Vienna': 684, 'Warsaw': 1138},
    'Brussels': {'Amsterdam': 173, 'Andorra': 952, 'Berlin': 652, 'Bern': 489, 'Brussels': 0, 'Lisbon': 1713, 'Luxembourg': 118, 'Madrid': 1317, 'Paris': 264, 'Rome': 1173, 'Vienna': 915, 'Warsaw': 1160},
    'Lisbon': {'Amsterdam': 1865, 'Andorra': 994, 'Berlin': 2316, 'Bern': 1627, 'Brussels': 1713, 'Lisbon': 0, 'Luxembourg': 1707, 'Madrid': 502, 'Paris': 1453, 'Rome': 1863, 'Vienna': 2299, 'Warsaw': 2759},
    'Luxembourg': {'Amsterdam': 319, 'Andorra': 865, 'Berlin': 604, 'Bern': 310, 'Brussels': 186, 'Lisbon': 1711, 'Luxembourg': 0, 'Madrid': 1279, 'Paris': 286, 'Rome': 988, 'Vienna': 764, 'Warsaw': 1080},
    'Madrid': {'Amsterdam': 1481, 'Andorra': 494, 'Berlin': 1869, 'Bern': 1152, 'Brussels': 1316, 'Lisbon': 502, 'Luxembourg': 1279, 'Madrid': 0, 'Paris': 1052, 'Rome': 1364, 'Vienna': 1809, 'Warsaw': 2289},
    'Paris': {'Amsterdam': 430, 'Andorra': 709, 'Berlin': 880, 'Bern': 434, 'Brussels': 263, 'Lisbon': 1452, 'Luxembourg': 286, 'Madrid': 1052, 'Paris': 0, 'Rome': 1105, 'Vienna': 1033, 'Warsaw': 1366},
    'Rome': {'Amsterdam': 1296, 'Andorra': 908, 'Berlin': 522, 'Bern': 684, 'Brussels': 1173, 'Lisbon': 1863, 'Luxembourg': 988, 'Madrid': 1364, 'Paris': 1105, 'Rome': 0, 'Vienna': 761, 'Warsaw': 1310},
    'Vienna': {'Amsterdam': 937, 'Andorra': 1321, 'Berlin': 880, 'Bern': 434, 'Brussels': 915, 'Lisbon': 2299, 'Luxembourg': 764, 'Madrid': 1809, 'Paris': 1033, 'Rome': 761, 'Vienna': 0, 'Warsaw': 553},
    'Warsaw': {'Amsterdam': 1096, 'Andorra': 1816, 'Berlin': 517, 'Bern': 1138, 'Brussels': 1160, 'Lisbon': 2759, 'Luxembourg': 1080, 'Madrid': 2289, 'Paris': 1366, 'Rome': 1310, 'Vienna': 553, 'Warsaw': 0}
}

# Tabla A*
# [0]: Distancia real, [1:-1]: Ruta
routes_cities = [
    [657, 'Amsterdam', 'Berlin'],
    [881, 'Amsterdam', 'Brussels', 'Luxembourg', 'Bern'],
    [210, 'Amsterdam', 'Brussels'],
    [2258,'Amsterdam', 'Brussels', 'Paris', 'Lisbon'],
    [434, 'Amsterdam', 'Brussels', 'Luxembourg'],
    [1797, 'Amsterdam', 'Brussels', 'Paris', 'Madrid'],
    [522, 'Amsterdam', 'Brussels', 'Paris'],
    [1732, 'Amsterdam', 'Brussels', 'Luxembourg', 'Bern', 'Rome'],
    [1145, 'Amsterdam', 'Vienna'],
    [1231, 'Amsterdam', 'Berlin', 'Warsaw'],
    #Andorra
    [1386, 'Andorra', 'Paris', 'Brussels', 'Amsterdam'],
    [2000, 'Andorra', 'Paris', 'Luxembourg', 'Berlin'],
    [1044, 'Andorra', 'Bern'],
    [1176, 'Andorra', 'Paris', 'Brussels'],
    [1252, 'Andorra', 'Madrid', 'Lisbon'],
    [1237, 'Andorra', 'Paris', 'Luxembourg'],
    [619, 'Andorra', 'Madrid'],
    [864, 'Andorra', 'Paris'],
    [1385, 'Andorra', 'Rome'],
    [1988, 'Andorra', 'Bern', 'Vienna'],
    [2488, 'Andorra', 'Bern', 'Warsaw'],
    #Bern
    [956, 'Berlin', 'Bern'],
    [867, 'Berlin', 'Amsterdam', 'Brussels'],
    [2872, 'Berlin', 'Luxembourg', 'Paris', 'Lisbon'],
    [763, 'Berlin', 'Luxembourg'],
    [2411, 'Berlin', 'Luxembourg', 'Paris', 'Madrid'],
    [1136, 'Berlin', 'Luxembourg', 'Paris'],
    [1503, 'Berlin', 'Rome'],
    [681, 'Berlin', 'Vienna'],
    [574, 'Berlin', 'Warsaw'],
    #Bern
    [876, 'Bern', 'Paris', 'Brussels'],
    [876, 'Bern', 'Paris', 'Brussels'],
    [2296, 'Bern', 'Andorra', 'Madrid', 'Lisbon'],
    [447, 'Bern', 'Luxembourg'],
    [1663, 'Bern', 'Andorra', 'Madrid'],
    [564, 'Bern', 'Paris'],
    [851, 'Bern', 'Rome'],
    [944, 'Bern', 'Vienna'],
    [1444, 'Bern', 'Warsaw'],
    #Brussels
    [2048, 'Brussels', 'Paris', 'Lisbon'],
    [224, 'Brussels', 'Luxembourg'],
    [1587, 'Brussels', 'Paris', 'Madrid'],
    [312, 'Brussels', 'Paris'],
    [1522, 'Brussels', 'Luxembourg', 'Bern', 'Rome'],
    [1163, 'Brussels', 'Luxembourg', 'Vienna'],
    [1441, 'Brussels', 'Amsterdam', 'Berlin', 'Warsaw'],
    #Lisbon
    [2109, 'Lisbon', 'Paris', 'Luxembourg'],
    [633, 'Lisbon', 'Madrid'],
    [1736, 'Lisbon', 'Paris'],
    [2637, 'Lisbon', 'Madrid', 'Andorra', 'Rome'],
    [3048, 'Lisbon', 'Paris', 'Luxembourg', 'Vienna'],
    [3446, 'Lisbon', 'Paris', 'Luxembourg', 'Berlin', 'Warsaw'],
    #Luxembourg
    [1648, 'Luxembourg', 'Paris', 'Madrid'],
    [373, 'Luxembourg', 'Paris'],
    [1298, 'Luxembourg', 'Bern', 'Rome'],
    [939, 'Luxembourg', 'Vienna'],
    [1337, 'Luxembourg', 'Berlin', 'Warsaw'],
    #Madrid
    [1275, 'Madrid', 'Paris'],
    [2004, 'Madrid', 'Andorra', 'Rome'],
    [2587, 'Madrid', 'Paris', 'Luxembourg', 'Vienna'],
    [2985, 'Madrid', 'Paris', 'Luxembourg', 'Berlin', 'Warsaw'],
    #Paris
    [1415, 'Paris', 'Bern', 'Rome'],
    [1415,  'Paris', 'Bern', 'Rome'],
    [1710,  'Paris', 'Luxembourg', 'Berlin', 'Warsaw'],
    #Rome
    [1122, 'Rome', 'Vienna'],
    [1849, 'Rome', 'Vienna', 'Warsaw'],
    #Vienna
    [727, 'Vienna', 'Warsaw']
    
]

coor = {
    'Amsterdam': (52.3650, 4.8917),
    'Andorra': (42.5065, 1.5220),
    'Berlin': (52.5230, 13.4061),
    'Bern': (46.9480, 7.4474),
    'Brussels': (50.8470, 4.3568),
    'Lisbon': (38.7238, -9.1416),
    'Luxembour': (49.6116, 6.1323),
    'Madrid': (40.4158, -3.7042),
    'Paris': (48.8567, 2.3514),
    'Rome': (41.9048, 12.4886),
    'Vienna': (48.2086, 16.3768),
    'Warsaw': (52.2252, 20.9980),
}

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
    for city in cities:
        route += city + " -> "
    return route[0:-4].upper()

def obtain():
    return

def create_input_frame(container):
    cities_to_visit = [tk.BooleanVar(value=True)] # Lista de las ciudades que se van a visitar
    for i in range(12):
        cities_to_visit.append(tk.BooleanVar(value=False))
    check = [] # Lista en la que ordenamos los checkbox de la ventana
    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)

    # Origin city
    ttk.Label(frame, text='Origin city').grid(column=0, row=0, sticky=tk.W)
    combo = ttk.Combobox(frame, width=30, state='readonly')
    def origin_city_changed(event): # Función del evento de cambio de valor del combobox
        cities_to_visit[combo.current()].set(True)
        for i in range(len(check)):
            check[i].config(state=NORMAL)
        check[combo.current()].config(state=DISABLED)

    combo['values'] = ['Amsterdam', 'Andorra', 'Berlin', 'Bern', 'Brussels', 'Lisbon', 'Luxembourg', 'Madrid', 'Paris', 'Rome', 'Vienna', 'Warsaw'] # Valores del combobox
    combo.set('Amsterdam') # Inicializa en Amsterdam
    combo.bind("<<ComboboxSelected>>", origin_city_changed)
    combo.focus()
    combo.grid(column=1, row=0, sticky=tk.W)


    # Cities to visit
    ttk.Label(frame, text='Cities to visit').grid(column=0, row=1, sticky=tk.W)
    # Amsterdam
    check.append(ttk.Checkbutton(
        frame,
        text='Amsterdam',
        variable=cities_to_visit[0]),)
    check[0].grid(column=1, row=1, sticky=tk.W)
    check[0].config(state=DISABLED)
    # Andorra
    check.append(ttk.Checkbutton(
        frame,
        text='Andorra',
        variable=cities_to_visit[1]))
    check[1].grid(column=1, row=2, sticky=tk.W)
    # Berlin
    check.append(ttk.Checkbutton(
        frame,
        text='Berlin',
        variable=cities_to_visit[2]))
    check[2].grid(column=1, row=3, sticky=tk.W)
    # Bern
    check.append(ttk.Checkbutton(
        frame,
        text='Bern',
        variable=cities_to_visit[3]))
    check[3].grid(column=1, row=4, sticky=tk.W)
    # Brussels
    check.append(ttk.Checkbutton(
        frame,
        text='Brussels',
        variable=cities_to_visit[4]))
    check[4].grid(column=1, row=5, sticky=tk.W)
    # Lisbon
    check.append(ttk.Checkbutton(
        frame,
        text='Lisbon',
        variable=cities_to_visit[5]))
    check[5].grid(column=1, row=6, sticky=tk.W)
    # Luxembourg
    check.append(ttk.Checkbutton(
        frame,
        text='Luxembourg',
        variable=cities_to_visit[6]))
    check[6].grid(column=2, row=1, sticky=tk.W)
    # Madrid
    check.append(ttk.Checkbutton(
        frame,
        text='Madrid',
        variable=cities_to_visit[7]))
    check[7].grid(column=2, row=2, sticky=tk.W)
    # Paris
    check.append(ttk.Checkbutton(
        frame,
        text='Paris',
        variable=cities_to_visit[8]))
    check[8].grid(column=2, row=3, sticky=tk.W)
    # Rome
    check.append(ttk.Checkbutton(
        frame,
        text='Rome',
        variable=cities_to_visit[9]))
    check[9].grid(column=2, row=4, sticky=tk.W)
    # Vienna
    check.append(ttk.Checkbutton(
        frame,
        text='Vienna',
        variable=cities_to_visit[10]))
    check[10].grid(column=2, row=5, sticky=tk.W)
    # Warsaw
    check.append(ttk.Checkbutton(
        frame,
        text='Warsaw',
        variable=cities_to_visit[11]))
    check[11].grid(column=2, row=6, sticky=tk.W)

    def clear_all(origin:int = 0): # Función que quita la selección de todas las ciudades y asigna a Amsterdam como origen
        check[origin].config(state=DISABLED)
        for checks in check:
            checks.config(state=NORMAL)
        for city in cities_to_visit:
            city.set(False)
        check[origin].config(state=DISABLED)
        cities_to_visit[origin].set(True)
        combo.set(combo['values'][origin])

    def random_select(n:int = 8): # Función para seleccionar n ciudades al azar y selecciona una como origen
        indexes = []
        while len(indexes) < n:
            aux = randrange(0, 12, 1)
            if aux not in indexes:
                indexes.append(aux)
        origin = indexes[randrange(0, n, 1)]
        clear_all(origin)
        for i in indexes:
            cities_to_visit[i].set(True)

    def count_trues() -> int: # Función que retorna el número de ciudades seleccionadas
        trues = 0
        for city in cities_to_visit:
            if city.get(): trues += 1
        return trues

    def shortest_trip_obtain(): #  Función que lee las ciudades seleccionadas y retorna la ruta más corta
        if count_trues() > 8: # Validamos que se escojan menos de 9 ciudades
            messagebox.showwarning(title='Alert', message='More than 8 cities selected')
            return
        if count_trues() < 3: # Validamos que se escojan más de 2 ciudades
            messagebox.showwarning(title='Alert', message='Less than 3 cities selected')
            return
        to_visit = []
        for i in range(len(cities_to_visit) - 1): # Hacemos una lista con los nombres de las ciudades seleccionadas
            if cities_to_visit[i].get():
                to_visit.append(combo['values'][i])
        origin = combo['values'][combo.current()]
        to_visit.remove(origin)
        trip, distance = shortest_trip(origin, to_visit) # Llamamos al método de viaje más corto
        messagebox.showinfo(title='Route to take', message=f'Order: {route_str(trip)}\n\nTotal distance: {str(distance)} km')

    # Botones
    ttk.Button(frame, text='Obtain trip', command=shortest_trip_obtain).grid(column=3, row=0)
    ttk.Button(frame, text='8 Random', command=random_select).grid(column=3, row=2)
    ttk.Button(frame, text='Clear all', command=clear_all).grid(column=3, row=3)
    ttk.Button(frame, text='Quit', command=container.destroy).grid(column=3, row=7)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def main():
    root = tk.Tk()
    root.title('Quinceañera Eurotrip')
    root.eval('tk::PlaceWindow . center')
    root.resizable(0, 0)

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    root.mainloop()


if __name__ == "__main__":
    main()