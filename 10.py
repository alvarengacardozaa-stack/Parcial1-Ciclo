# EJERCICIO 10: isalnum() y separación

texto = "Python2026"
es_alfanumerico = texto.isalnum()

if es_alfanumerico:
    limpio = texto.lower().replace("2026", "")

    print(f"E10: {limpio}")
