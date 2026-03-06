Algoritmo CalificacionEstudiante
    Definir nota Como Real
    Escribir "Ingrese la nota del estudiante (0-10):"
    Leer nota
    
    // La validacion: La nota debe ser valida segun el sistema (0-10)
	
    Si nota >= 0 Y nota <= 10 Entonces
        Si nota >= 6 Entonces
            Escribir "Calificacion: Aprobado"
        Sino
            Si nota <= 4 Entonces
                Escribir "Calificacion: Reprobado"
            Sino
                Escribir "Calificacion: Recuperacion"
            FinSi
        FinSi
    Sino
        Escribir "Error: La nota ingresada no es valida. Debe estar entre 0 y 10."
    FinSi
	
FinAlgoritmo