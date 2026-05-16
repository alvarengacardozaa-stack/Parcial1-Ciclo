## Ejercicio n° 2.

# Las empresas pierden dinero por errores de redondeo al usar float.

from decimal import Decimal

total = Decimal("0.00")

while True:
    entrada = input("Ingrese el precio del producto (o '0' para finalizar): ")

    if entrada == "0":
        break

    try:

        monto = Decimal(entrada)
        total += monto
    except ValueError:

        print("Advertencia: Ingrese un número válido.")

print(f"Total acumulado: ${total}")
