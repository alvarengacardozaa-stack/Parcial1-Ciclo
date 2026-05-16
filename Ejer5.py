## Ejercicio n° 5.

# Para cumplir con la normativa de privacidad.

nombre_completo = input("Ingrese su nombre y apellido: ")

palabras = nombre_completo.split()
lista_invertida = palabras[::-1]

for palabra in lista_invertida:
    letras_formateadas = ""
    for letra in palabra:
        letras_formateadas += letra + "."

    print(letras_formateadas[:-1])
