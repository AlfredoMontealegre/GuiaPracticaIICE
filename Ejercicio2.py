import random

#Definir los dos laboratorios
laboratorios = ["Laboratorio A","laboratorio B" ]

#Bucle para conocer los espacios ocpuados y disponibles.
for lab in laboratorios:
    print(f"\n---{lab}---")
    ocupados = 0
    disponibles = 0
    
    #Preguntar si se desea ingresar datos manualmente o de forma aleatoria
    modo = input("Seleccione el modo de analisis: i = Ingresar, r = Randomizer ")    
    
    #Numero de filas y computadoras usadas
    for fila in range(1,6):
        print(f"\nFila: {fila}")
        for computadora in range (1,5):
            if modo == 'i':
                #Modo manual
                while True:
                    estado = int(input(f"¿La computadora está ocupada? 1 = Si, 0 = No "))
                    if estado in (0,1):
                        break
                    else:
                        print("Error... Selección no valida")
            else:
                #Modo simulado (Random)
                estado = random.randint(0,1)
                print(f"Computadora {computadora}: {'Ocupada' if estado == 1 else 'Libre'}")
        
        #Acumulación de datos del bucle
        if estado == 1:
            ocupados += 1
        else:
            disponibles += 1
    
    #Devolver datos (Libres y ocupados)
    print(f"\nResumen en {lab}:")
    print(f"Computadoras ocupadas: {ocupados}")
    print(f"Computadoras libres: {disponibles}")