import numpy as np

#### DATOS PARA EL ENTRENAMIENTO ####

# Datos de 10 personas -> [edad, ahorro]
personas = np.array([[0.3, 0.4], [0.4, 0.3],
                     [0.3, 0.2], [0.4, 0.1], 
                     [0.5, 0.2], [0.4, 0.8],
                     [0.6, 0.8], [0.5, 0.6], 
                     [0.7, 0.6], [0.8, 0.5]])
# 1 : aprobrada    0 : denegada
clases = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

### FUNCIÓN DE ACTIVACIÓN ###

# w1*x1 + w2*x2 + ⋯ + wn*xn

def activacion(w, x, b):
    z = w * x
    if z.sum() + b > 0:
        return 1
    else:
        return 0
    
### ENTRENAMIENTO ###

pesos = np.random.uniform(-1, 1, size=2)
b = np.random.uniform(-1, 1)
tasa_de_aprendizaje = 0.01
epocas = 100

for epoca in range(epocas):
    for i in range(len(personas)):
        prediccion = activacion(pesos, personas[i], b)
        error = clases[i] - prediccion
        pesos[0] += tasa_de_aprendizaje * personas[i][0] * error
        pesos[1] += tasa_de_aprendizaje * personas[i][1] * error
        b += tasa_de_aprendizaje * error

### PROBAR ###
while True:
    try:
        edad = float(input("Edad: "))
        ahorro = float(input("Ahorro: "))

        print(f"\n{'Autorizar' if activacion(pesos, [edad, ahorro], b) == 1 else 'No autorizar'}\n")
    except:
        next
    