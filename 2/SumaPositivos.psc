Algoritmo SumaPositivos
	
    Definir nume, suma Como Real
    suma <- 0
    
    Repetir
        Escribir "Ingrese un numero (ingrese un negativo para terminar y ver el total):"
        Leer nume
        
        // Validacion: Solo sumamos si el numero es positivo
		
        Si nume >= 0 Entonces
            suma <- suma + nume
        FinSi
	Hasta Que nume < 0 
	//La condicion de salida es un numero negativo 
    
    Escribir "La suma total de todos los numeros positivos ingresados es: ", suma 
	
FinAlgoritmo