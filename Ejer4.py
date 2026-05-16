## Ejercicio n° 4.

# Un script debe auditar una secuencia de 50 registros.

for id_registro in range(1, 51):

    if id_registro % 3 == 0:
        continue

    if id_registro == 42:
        print("¡Brecha de seguridad detectada! Deteniendo proceso...")
        break

    print(f"Procesando registro ID: {id_registro}")
