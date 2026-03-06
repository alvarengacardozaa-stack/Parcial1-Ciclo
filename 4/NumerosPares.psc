Algoritmo NumerosPares
	
    Definir n, i Como Entero
    Escribir "Ingrese cuantos numeros pares desea ver:"
    Leer n
    
    // La validacion: N debe ser un entero positivo
    Si n > 0 Entonces
        Para i <- 1 Hasta n Hacer
            Escribir "Par ", i, ": ", i * 2
        FinPara
    Sino
        Escribir "Error: Debe ingresar un numero entero positivo mayor a cero."
    FinSi
	
FinAlgoritmo