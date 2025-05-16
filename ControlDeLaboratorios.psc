Proceso ControlDeLaboratorios
	
    Definir ocupados, disponibles, estado, fila, computadora Como Entero
    Definir modo, laboratorio Como Cadena
	
    // Bucle para recorrer los dos laboratorios
    Para num_lab <- 1 Hasta 2 Hacer
		
        Si num_lab = 1 Entonces
            laboratorio <- "Laboratorio A"
        Sino
            laboratorio <- "Laboratorio B"
        FinSi
		
        Escribir ""
        Escribir "--- ", laboratorio, " ---"
        ocupados <- 0
        disponibles <- 0
		
        // Elegir modo
        Escribir "Seleccione el modo de análisis: i = Ingresar, r = Randomizer"
        Leer modo
		
        // Bucle de filas (1 a 5)
        Para fila <- 1 Hasta 5 Hacer
            Escribir ""
            Escribir "Fila: ", fila
			
            // Bucle de computadoras (1 a 4)
            Para computadora <- 1 Hasta 4 Hacer
				
                Si modo = "i" Entonces
                    // Modo manual
                    Repetir
                        Escribir "¿La computadora está ocupada? 1 = Sí, 0 = No: "
                        Leer estado
                        Si estado <> 0 Y estado <> 1 Entonces
                            Escribir "Error... Selección no válida"
                        FinSi
                    Hasta Que estado = 0 O estado = 1
					
                Sino
                    // Modo random (simulado)
                    estado <- Aleatorio(0,1)
                    Si estado = 1 Entonces
                        Escribir "Computadora ", computadora, ": Ocupada"
                    Sino
                        Escribir "Computadora ", computadora, ": Libre"
                    FinSi
					
                FinSi
				
                // Contabilizar
                Si estado = 1 Entonces
                    ocupados <- ocupados + 1
                Sino
                    disponibles <- disponibles + 1
                FinSi
				
            FinPara
			
        FinPara
		
        // Resumen de resultados por laboratorio
        Escribir ""
        Escribir "Resumen en ", laboratorio, ":"
        Escribir "Computadoras ocupadas: ", ocupados
        Escribir "Computadoras libres: ", disponibles
		
    FinPara
	
FinAlgoritmo