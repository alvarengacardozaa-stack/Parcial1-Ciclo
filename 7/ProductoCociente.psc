Algoritmo ProductoCociente
	
    Definir numero1, numero2, producto, cociente Como Real
    Escribir "Ingrese el primer numero:"
    Leer numero1
    Escribir "Ingrese el segundo numero (divisor):"
    Leer numero2
    
    producto <- numero1 * numero2
    Escribir "El producto es: ", producto
    
    // validacion: el segundo numero no puede ser cero para la division
	
    Si numero2 <> 0 Entonces
        cociente <- numero1 / numero2
        Escribir "El cociente es: ", cociente
    Sino
        Escribir "Error: No es posible realizar la division porque el divisor es 0."
    FinSi
	
FinAlgoritmo