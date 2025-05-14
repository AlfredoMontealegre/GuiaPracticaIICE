# Ejercicio 3: Programa para controlar las ventas en una feria universitaria


# Declarar las variables principales
dias = 3
stands_por_dia = 4
productos_por_stand = 3

# Crear una lista para guardar las ventas
ventas = []

# Recolectar datos
for dia in range(dias):
    print("Día", dia + 1)
    ventas_dia = []
    for stand in range(stands_por_dia):
        print("  Stand", stand + 1)
        ventas_stand = []
        for producto in range(productos_por_stand):
            venta = float(input("    Ingrese la venta del producto " + str(producto + 1) + ": "))
            ventas_stand.append(venta)
        ventas_dia.append(ventas_stand)
    ventas.append(ventas_dia)

# Mostrar resumen de ventas
total_general = 0

for dia in range(dias):
    print("\nResumen del Día", dia + 1)
    total_dia = 0
    for stand in range(stands_por_dia):
        total_stand = sum(ventas[dia][stand])
        print("  Stand", stand + 1, "- Total ventas: $", round(total_stand, 2))
        total_dia += total_stand
    print("  Total del Día", dia + 1, ": $", round(total_dia, 2))
    total_general += total_dia

# Mostrar total general
print("\nTotal general de la feria: $", round(total_general, 2))
