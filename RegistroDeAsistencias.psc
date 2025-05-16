Proceso RegistroDeAsistencias
	
    Definir asistencias_totales, asistencias_seccion, asistencia, dia, estudiante Como Entero
    Definir seccion Como Cadena
    asistencias_totales <- 0
	
    // Bucle externo (Secciones)
    Para num_seccion <- 1 Hasta 3 Hacer
        
        Si num_seccion = 1 Entonces
            seccion <- "c-101"
        Sino
            Si num_seccion = 2 Entonces
                seccion <- "b-202"
            Sino
                seccion <- "m-303"
            FinSi
        FinSi
		
        Escribir ""
        Escribir "+++ ", seccion, " +++"
        asistencias_seccion <- 0
		
        // Bucle de días (1 a 5)
        Para dia <- 1 Hasta 5 Hacer
            Escribir ""
            Escribir "Día: ", dia
			
            // Bucle de los 6 estudiantes
            Para estudiante <- 1 Hasta 6 Hacer
                Repetir
                    Escribir "¿Asistió a clases el estudiante ", estudiante, "? 1 = Sí  0 = No: "
                    Leer asistencia
                    Si asistencia <> 1 Y asistencia <> 0 Entonces
                        Escribir "¡¡ERR000R!! Ingrese 1 o 0"
                    FinSi
                Hasta Que asistencia = 1 O asistencia = 0
				
                asistencias_seccion <- asistencias_seccion + asistencia
				
            FinPara
			
        FinPara
		
        // Mostrar total de asistencias por sección
        Escribir ""
        Escribir "Total de asistencias en la sección ", seccion, ": ", asistencias_seccion
        asistencias_totales <- asistencias_totales + asistencias_seccion
		
    FinPara
	
    // Mostrar las asistencias totales
    Escribir ""
    Escribir "El total de asistencias en todas las secciones durante esta semana es: ", asistencias_totales
	
FinAlgoritmo



