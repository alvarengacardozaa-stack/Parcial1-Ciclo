# EJERCICIO 7: zfill() y endswith()

texto = "42"
relleno = texto.zfill(5)
termina_en = relleno.endswith("2")

print(f"E7: {relleno}, ¿termina en 2?: {termina_en}")
