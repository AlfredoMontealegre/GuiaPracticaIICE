"""
Ejercicio 4: Monitoreo del consumo energético
Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
generar el promedio semanal correspondiente.
"""

# Control de Cantidades
# Semana = 7 dias
# Turnos = 3 turnos
# Edificios = 4 edificios
# Serian 4 series de 7 dias y 3 turnos en cada dia.

edificios = 4
dias = 7
turnos = 3

# El consumo total quedria guardado aqui, esto para que posterior a los datos
# Luego se le sumen y almacenen para sacar el consumo final.
consumos_totales = []

# Se hacen la serie de 4 edificios para que se registre
# Asi como que fueran clientes, un registro por edificio. (1-4)
for i in range(edificios):
    print(f"Edificio #{i + 1}")
    consumo_sem = 0

    # En esta parte se ponen la serie de los 7 dias para que repitan
    # Preguntaria desde el dia 1, hasta el dia 7.
    for o in range(dias):
        print(f"Dia #{o + 1}")
        print("Mañana = 0 | Tarde = 1 | Noche = 2")
        consumo_dia = 0

        # Aqui los datos no son numeros, son palabras, asi que usariamos float
        # De esta manera localiza los datos mañana, tarde, noche y asi los pone en orden
        # Primero pregunta de dia, luego tarde, luego noche y repite posteriormente.
        for turno in range(turnos):
            consumo = float(input(f"Ingrese consumo en {turno} (kWh): "))
            consumo_dia += consumo

        consumo_sem += consumo_dia
    
    consumos_totales.append(consumo_sem)
        
# Finalmente esto seria el output, lo que se va a mostrar de resultados finales a el calculo
print("Resultados de cada edificio: ")
for i in range(edificios):
    total = consumos_totales[i]
    promedio = total / dias
    print(f"Edificio {i + 1}: Total = {total:.2f} kWh | Promedio diario = {promedio:.2f} kWh")
