import random #Importar la librería random para así generar números aleatorios

#Lista de laboratorios
laboratorios = ["Laboratorio A","laboratorio B" ]

#Bucle externo: Encargado de recorrer los dos laboratorios en la lista
for lab in laboratorios:
    print(f"\n---{lab}---")
    
    #Variables para almacenar la información correspondiente
    ocupados = 0
    disponibles = 0
    
    #Solicitud de si se desea ingresar datos manualmente o de forma aleatoria
    modo = input("Seleccione el modo de analisis: i = Ingresar, r = Randomizer ")
    
    #Validación de selección de modo manual
    while modo not in ('i', 'r'):
        modo = input("Modo inválido. Seleccione: i = Ingresar, r = Randomizer ")
    
    #Bucle medio: Encargado de recorrer el número de filas a regirstrar
    for fila in range(1,6):
        print(f"\nFila: {fila}")
        
        #Bucle interno encargado de recorrer las 4 computadoras por fila
        for computadora in range (1,5):
            
            #Comando por si se seleccionó el modo manual
            if modo == 'i':
                
                #Validación de estado de computadoras (Si se ingresa de forma manual los datos)
                while True:
                    estado = int(input(f"¿La computadora está ocupada? 1 = Si, 0 = No "))
                    if estado in (0,1):
                        break
                    
                    #En caso de no ingresar los valores asignados se ejecutara este comando:
                    while estado not in (0,1):
                        print(f"\n¡¡ERR0R!! intentelo de nuevo")
                        break
            else:
                #Modo simulado (Random)
                estado = random.randint(0,1)
                print(f"Computadora {computadora}: {'Ocupada' if estado == 1 else 'Libre'}")
        
        #Acumulación de datos del bucle
        #Si el estado es igual a 1.
        #Se almacenara en la variable "Ocupados"
        if estado == 1:
            ocupados += 1
            
        #Si el estado es igual a 0
        #La información se almacenará en la variable "Disponibles"
        else:
            disponibles += 1
    
    #Devolver datos 
    # Resumenes de ambos laboratorios y que espacios están libres y ocupados
    print(f"\nResumen en {lab}:")
    print(f"Computadoras ocupadas: {ocupados}")
    print(f"Computadoras libres: {disponibles}")