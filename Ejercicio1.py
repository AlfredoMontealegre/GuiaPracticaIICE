#Lista que se encarga de definir las secciones de la universidad
secciones = ["c-101", "b-202", "m-303"]

#Variable que permite guardar el total de asistencias acumuladas
asistencias_totales = 0

#Bucle externo encargado de recorrer cada sección en la lista
for seccion in secciones:
    print(f"n\+++{seccion}+++")
    asistencias_seccion = 0
    
    #Bucle encargado de recorrer los días de la semana
    for dia in range (1,6):
        print(f"\n Día: {dia}")
        
        #bucle encargado de recorrer los 6 estudiantes de la lista.
        for estudiante in range(1,7):
            
            #Validación de entrada: Para marcar la asistencia de los estudiantes.
            while True:
                asistencia = int(input(f"¿Asistio a clases el estudiante {estudiante}? 1 = Sí 0 = No "))
                if asistencia in (1,0):
                    break
                else:
                    print("¡¡ERR000R!! Ingrese 1 o 0")
            
            #Sumatoria que va acumulando las asistencias en la variable de asistencias por sección
            asistencias_seccion += asistencia
            
    #Mostrar todas las asistencias por sección
    print(f"\n Total de asistencias en la sección {seccion}: {asistencias_seccion}")
    
    #Sumatoria de todas las asistencias por sección para así acumularlas en la variable general
    asistencias_totales += asistencias_seccion

#Mostrar las asistencias totales (Sumatoria total de las asistencias en todas las secciones)
print(f"\nEl total de asistencias en todas las secciones durante esta semana es {asistencias_totales}")