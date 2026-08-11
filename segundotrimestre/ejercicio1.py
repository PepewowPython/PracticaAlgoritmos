#@author: Jeremy Chica Tapasco
# @descripcion: Ejercicio 1 - Prueba piloto de producción de plantas (7 días)
# @requisitos:
#   - 10 plantas en Colombia (planta_MED, planta_CAL, planta_BOG, etc.)
#   - Ingresar y validar el nombre de la planta.
#   - Ingresar y validar producción de 7 días consecutivos (rango 100 - 1000 unidades).
#   - Guardar en un vector (lista).
#   - Calcular y mostrar: día de menor producción, día de mayor producción, total y promedio.

# Lista oficial de las 10 plantas y sus correspondientes ciudades
PLANTAS_VALIDAS = {
    "MED": "planta_MED",
    "CAL": "planta_CAL",
    "BOG": "planta_BOG",
    "CUC": "planta_CUC",
    "PER": "planta_PER",
    "MAN": "planta_MAN",
    "GUA": "planta_GUA",
    "ARM": "planta_ARM",
    "BAR": "planta_BAR",
    "CAR": "planta_CAR"
}

NOMBRES_CIUDADES = {
    "MEDELLIN": "planta_MED",
    "MEDELLÍN": "planta_MED",
    "CALI": "planta_CAL",
    "BOGOTA": "planta_BOG",
    "BOGOTÁ": "planta_BOG",
    "CUCUTA": "planta_CUC",
    "CÚCUTA": "planta_CUC",
    "PEREIRA": "planta_PER",
    "MANIZALES": "planta_MAN",
    "GUARNE": "planta_GUA",
    "ARMENIA": "planta_ARM",
    "BARRANQUILLA": "planta_BAR",
    "CARTAGENA": "planta_CAR"
}


def solicitar_nombre_planta():
    """Solicita y valida el nombre de la planta ingresado por teclado."""
    print("=== REGISTRO DE PLANTA ===")
    print("Plantas disponibles:")
    for cod, nombre in PLANTAS_VALIDAS.items():
        print(f" - {nombre}")

    while True:
        entrada = input("\nIngrese el nombre de la planta (ej. planta_MED o Medellín): ").strip()
        entrada_clean = entrada.upper()

        # Verificar si coincide directamente con el nombre completo (ej: PLANTA_MED)
        if entrada_clean in [p.upper() for p in PLANTAS_VALIDAS.values()]:
            # Retornar en formato estandarizado
            for p in PLANTAS_VALIDAS.values():
                if p.upper() == entrada_clean:
                    return p

        # Verificar si ingresó la abreviatura o ciudad
        if entrada_clean in PLANTAS_VALIDAS:
            return PLANTAS_VALIDAS[entrada_clean]

        if entrada_clean in NOMBRES_CIUDADES:
            return NOMBRES_CIUDADES[entrada_clean]

        print("ERROR: Nombre de planta no válido. Por favor, intente de nuevo.")


def solicitar_produccion_diaria(dia):
    """Solicita y valida la producción de un día específico (rango 100 a 1000)."""
    while True:
        try:
            valor = float(input(f"Ingrese la producción del Día {dia} (100 - 1000 unidades): "))
            if 100 <= valor <= 1000:
                return valor
            else:
                print("ERROR: La producción debe estar entre 100 y 1000 unidades.")
        except ValueError:
            print("ERROR: Ingrese un valor numérico válido.")


def main():
    print("==================================================")
    print("   SISTEMA DE CONTROL DE PRODUCCIÓN - PRUEBA PILOTO")
    print("==================================================\n")

    # 1. Ingreso y validación del nombre de la planta
    nombre_planta = solicitar_nombre_planta()
    print(f"\nPlanta seleccionada: {nombre_planta}")

    # 2. Ingreso y validación de la producción de 7 días (almacenados en un vector)
    produccion_dias = []
    print("\n--- INGRESO DE PRODUCCIÓN DIARIA (7 DÍAS CONSECUTIVOS) ---")
    for dia in range(1, 8):
        cant = solicitar_produccion_diaria(dia)
        produccion_dias.append(cant)

    # 3. Cálculos de reporte
    total_produccion = sum(produccion_dias)
    promedio_produccion = total_produccion / len(produccion_dias)

    min_prod = min(produccion_dias)
    max_prod = max(produccion_dias)

    dia_menor = produccion_dias.index(min_prod) + 1
    dia_mayor = produccion_dias.index(max_prod) + 1

    # 4. Mostrar reporte final
    print("\n==================================================")
    print(f"      REPORTE FINAL PILOTO - {nombre_planta}")
    print("==================================================")
    print(f"Vector de Producción (Días 1 al 7): {produccion_dias}")
    print("--------------------------------------------------")
    print(f"• Día de MENOR producción : Día {dia_menor} con {min_prod:.2f} unidades")
    print(f"• Día de MAYOR producción : Día {dia_mayor} con {max_prod:.2f} unidades")
    print(f"• Total producción        : {total_produccion:.2f} unidades")
    print(f"• Promedio diario         : {promedio_produccion:.2f} unidades/día")
    print("==================================================")


if __name__ == "__main__":
    main()
