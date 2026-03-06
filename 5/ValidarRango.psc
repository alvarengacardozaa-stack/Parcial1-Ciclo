Algoritmo ValidarRango
	
	Escribir "Estas atrapado en el lugar que siempre quisiste pero sabes que no es real"
    Definir numeroIngresado Como Real
    Escribir "Ingresa un numero entre 1 y 10 si quieres seguir aqui (Ingresa cualquier otro para encontrar una saida):"
    Leer numeroIngresado
    
    Mientras (numeroIngresado >= 1 Y numeroIngresado <= 10) Hacer
        Escribir "numero ", numeroIngresado, " es valido. Ingrese otro para continar:"
        Leer numeroIngresado
    FinMientras
    
    Escribir "Lograste encontrar una salida."
	
FinAlgoritmo