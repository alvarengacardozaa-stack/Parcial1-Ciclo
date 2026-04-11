# EJERCICIO 4: lower(), removesuffix() y find()
texto = "CANTANDO"
minusculas = texto.lower()

sin_sufijo = minusculas.removesuffix("ando")
indice = sin_sufijo.find("t")

# C A N T
# 0 1 2 3

print(f"E4 {sin_sufijo}, Indice de 't': {indice}")
