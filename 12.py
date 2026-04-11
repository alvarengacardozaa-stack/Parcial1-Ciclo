# EJERCICIO 12: prefijos/sufijos y minúsculas

archivo12 = "Sunombre.txt"

# Nota: La indicación pide remover prefijo "ING. ", aunque no esté en la cadena original

nombre_limpio12 = archivo12.removesuffix(".txt").removeprefix("ING. ").lower()

print(f"E12: {nombre_limpio12}")
