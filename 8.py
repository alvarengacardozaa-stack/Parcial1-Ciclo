# EJERCICIO 8: count() y splitlines()

poema = """Amor prohibido

Subes centelleante de labios y de ojeras!
Por tus venas subo, como un can herido
que busca el refugio de blandas aceras.

Amor, en el mundo tú eres un pecado!
Mi beso en la punta chispeante del cuerno
del diablo; mi beso que es credo sagrado!

Espíritu en el horópter que pasa
¡puro en su blasfemia!
¡el corazón que engendra al cerebro!
que pasa hacia el tuyo, por mi barro triste.
¡Platónico estambre
que existe en el cáliz donde tu alma existe!

¿Algún penitente silencio siniestro?
¿Tú acaso lo escuchas? Inocente flor!
… Y saber que donde no hay un Padrenuestro,
el Amor es un Cristo pecador!"""

conteo = poema.count("a")
lista_lineas = poema.splitlines()

print(f"E8: Conteo 'a': {conteo}, Líneas: {lista_lineas}")
