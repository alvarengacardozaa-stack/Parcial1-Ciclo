## Ejercicio n° 1.

# Se trabaja para una empresa de envíos.

etiqueta = input("Ingrese la etiqueta de rastreo (AÑO-CATEGORÍA-PAÍS): ")

if not etiqueta:
    print("Error: La entrada no puede estar vacía.")
    exit()

partes = etiqueta.split("-")
categoria = partes[1] if len(partes) > 1 else "Desconocida"
print(f"Categoría extraída: {categoria}")

ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
print(ruta)
