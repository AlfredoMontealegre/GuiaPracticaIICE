# Ejercicio 3: Programa para controlar las ventas en una feria universitaria



# Función para ingresar ventas
def ingresar_ventas(dia, stand):
    total = 0
    for i in range(1, 4):  # Tres productos por stand
        total += float(input(f"Día {dia} - Stand {stand} - Producto {i}: "))
    return total

# Variables de total por día
total_general = 0

# Recolectar ventas para 3 días
for dia in range(1, 4):
    total_dia = 0
    print(f"\n=== Día {dia} ===")
    for stand in range(1, 5):  # 4 stands por día
        total_stand = ingresar_ventas(dia, stand)
        total_dia += total_stand
        print(f"Stand {stand} - Total: ${round(total_stand, 2)}")
    total_general += total_dia
    print(f"Total Día {dia}: ${round(total_dia, 2)}")

print("\nTotal General: $", round(total_general, 2))
