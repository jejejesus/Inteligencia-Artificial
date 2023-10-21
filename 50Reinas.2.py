import sys
import random

class Tablero:
    def _init_(self, dato):
        self.vector = dato
        self.totalAtaques = None

def contarAtaques(v):
    ataques = 0
    n = len(v)
    for i in range(n):
        for j in range(i + 1, n):
            if v[i] == v[j] or abs(i - j) == abs(v[i] - v[j]):
                ataques += 2
    return ataques

def goalTest(v):
    return contarAtaques(v) == 0

def expand(tablero):
    n = len(tablero.vector)
    hijos = []
    for i in range(n):
        aux = tablero.vector.copy()
        for j in range(n):
            if (tablero.vector[i] + 1) < n and aux[i] + 1 < n:
                aux[i] = aux[i] + 1
                hijos.append(Tablero(aux.copy()))
            else:
                r = random.randint(0, n - 1)
                aux[i] = r
                hijos.append(Tablero(aux.copy()))
    return hijos

def Evaluate(os):
    for tablero in os:
        tablero.totalAtaques = contarAtaques(tablero.vector)
    return os

def Sort(os):
    min_ataques = min(tablero.totalAtaques for tablero in os)
    candidatos = [tablero for tablero in os if tablero.totalAtaques == min_ataques]
    return [random.choice(candidatos)]

def busquedaVoraz(f):
    if len(f) == 0:
        print("No se encontró resultado")
        return False
    else:
        edo_act = f.pop(0)
        print(edo_act.vector)

    if goalTest(edo_act.vector):
        print("Se encontró una solución:")
        print(edo_act.vector)
        return True

    os = expand(edo_act)
    os = Evaluate(os)
    os.sort(key=lambda tablero: tablero.totalAtaques)

    if len(os) > 0:
        os = Sort(os)
        f = [os[0]]

    return busquedaVoraz(f)

sys.setrecursionlimit(1000000)

v = [0] * 50
t = Tablero(v)
t.totalAtaques = contarAtaques(t.vector)
f = [t]

busquedaVoraz(f)