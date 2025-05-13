#Definir las secciones
secciones = ["c-101", "b-202", "m-303"]

#Total de asistencias acumuladas
asistencias_totales = 0

#Bucle externo (Secciones)
for seccion in secciones:
    print(f"n\+++{seccion}+++")
    asistencias_seccion = 0
    
    #bucle de días
    for dia in range (1,6):
        print(f"\n Día: {dia}")
        
        #bucle de los 6 estudiantes seleccionados.
        for estudiante in range(1,7):
            while True:
                asistencia = int(input(f"¿Asistio a clases el estudiante {estudiante}? 1 = Sí 0 = No "))
                if asistencia in (1,0):
                    break
                else:
                    print("¡¡ERR000R!! Ingrese 1 o 0")
                
            asistencias_seccion += asistencia
            
    #Mostrar todas las asistencias por sección
    print(f"\n Total de asistencias en la sección {seccion}: {asistencias_seccion}")
    asistencias_totales += asistencias_seccion

#Mostrar las asistencias totales (Sumatoria total de las asistencias en todas las secciones)
print(f"\nEl total de asistencias en todas las secciones durante esta semana es {asistencias_totales}")