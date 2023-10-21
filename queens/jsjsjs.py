def imprimir_tablero_vertical(posiciones):
  """Imprime una tabla con la posición de las reinas de ajedrez, con las columnas verticalmente."""

  # Imprime la cabecera de la tabla
  for i in range(8):
    print(f"{chr(ord('A') + i):^2}", end="")
  print()

  # Imprime las filas de la tabla
  for i in range(8):
    for j in posiciones:
      if j == i:
        print("R", end="")
      else:
        print("-", end="")
    print()


# Ejemplo de uso
posiciones = [1, 3, 5, 7, 2, 4, 6, 8]
imprimir_tablero_vertical(posiciones)