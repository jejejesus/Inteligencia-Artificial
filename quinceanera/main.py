import tkinter as tk
from random import randrange
from tkinter import ttk, DISABLED, NORMAL, messagebox
from trip import shortest_trip, route_str

def obtain():
    return

def create_input_frame(container):

    origin_city = tk.StringVar

    cities_to_visit = [tk.BooleanVar(value=True)]
    for i in range(12):
        cities_to_visit.append(tk.BooleanVar(value=False))

    check = []

    frame = ttk.Frame(container)
    

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)

    # Origin city
    ttk.Label(frame, text='Origin city').grid(column=0, row=0, sticky=tk.W)
    combo = ttk.Combobox(frame, width=30, textvariable=origin_city, state='readonly')
    def origin_city_changed(event): 
        cities_to_visit[combo.current()].set(True)
        for i in range(len(check)):
            check[i].config(state=NORMAL)
        check[combo.current()].config(state=DISABLED)

    combo['values'] = ['Amsterdam', 'Andorra', 'Berlin', 'Bern', 'Brussels', 'Lisbon', 'Luxembourg', 'Madrid', 'Paris', 'Rome', 'Vienna', 'Warsaw']
    combo.set('Amsterdam')
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

    def clear_all(origin:int = 0):
        check[origin].config(state=DISABLED)
        for checks in check:
            checks.config(state=NORMAL)
        for city in cities_to_visit:
            city.set(False)
        check[origin].config(state=DISABLED)
        cities_to_visit[origin].set(True)
        combo.set(combo['values'][origin])

    def random_select(n:int = 8):
        indexes = []
        while len(indexes) < n:
            aux = randrange(0, 12, 1)
            if aux not in indexes:
                indexes.append(aux)
        origin = indexes[randrange(0, n, 1)]
        clear_all(origin)
        for i in indexes:
            cities_to_visit[i].set(True)

    def shortest_trip_obtain():
        to_visit = []
        for i in range(len(cities_to_visit) - 1):
            if cities_to_visit[i].get():
                to_visit.append(combo['values'][i])
        origin = combo['values'][combo.current()]
        to_visit.remove(origin)
        trip, distance = shortest_trip(origin, to_visit)
        messagebox.showinfo(title='Route to take', message=f'Order: {route_str(trip)}\n\nTotal distance: {str(distance)} km')

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