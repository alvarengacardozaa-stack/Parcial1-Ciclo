## Ejercicio n° 3.

# Un sensor industrial envía lecturas de temperatura.

temperaturas = []

for i in range(5):
    temperatura = int(input(f"Ingese lectura de temperatura {i+1}: "))
    temperaturas.append(temperatura)


for t in temperaturas:
    match t:
        case 0:
            print(f"{t}: Alerta: Punto de Congelación")
        case 100:
            print(f"{t}: Alerta: Punto de Ebullición")
        case _:

            estado = "Estado: Estable" if 10 <= t <= 30 else "Estado: Crítico"
            print(f"{t}: {estado}")
