from trip import shortest_trip
import tkinter as tk

def main(): # Método main
    aux = shortest_trip('Andorra', ['Brussels', 'Amsterdam', 'Paris'])
    print(aux)

if __name__ == "__main__":
    main()