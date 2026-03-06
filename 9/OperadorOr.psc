Algoritmo OperadorOr
	
    Definir dinero Como Entero
    Escribir "Ingrese un numero entero para verificar divisibilidad (3 o 5):"
    Leer dinero
    
    // Validacion implicita al definir num como Entero. 
    // Si el usuario ingresa un real, PSeInt lo truncara o dara error segun el perfil.
	
    Si (dinero % 3 = 0) O (dinero % 5 = 0) Entonces
        Escribir "Resultado: Verdadero (Es divisible, Yai) :)"
    Sino
        Escribir "Resultado: Falso (No es divisible por ninguno, ahhh) :("
    FinSi
	
FinAlgoritmo