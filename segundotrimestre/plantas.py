#@Descripción: Una empresa de producción tiene 10 plantas 
#               distribuidas en 10 ciudades de Colombia: 
#               Medellín, Cali, Bogotá, Cúcuta, Pereira, 
#               Manizales, Guarne, Armenia, Barranquilla y 
#               Cartagena.  Cada planta se denomina con las 
#               tres primeras letras del nombre así: planta_MED 
#               para Medellín, planta_CAL para Cali y así 
#               sucesivamente. 
# Se debe realizar una prueba piloto sobre una de las plantas 
# para posteriormente realizarla en las demás plantas.  
# La prueba consiste en realizar un reporte de la producción 
# de una planta en 7 días consecutivos. 
# Se debe obtener: el día de menor producción, el día de mayor 
# producción, el total de producción de la planta y el promedio 
# de producción de ésta.
# Los datos del nombre de la planta y la producción de los 
# siete días deben ser ingresados por teclado y almacenados 
# en un vector.  
# Se debe validar toda la información que se ingrese
# por teclado. 
# Se sabe de antemano que la producción de las plantas está 
# en el rango de 100 a 1000 unidades por día.
# Realizar un programa en Python que refleje las necesidades 
# iniciales de la empresa.
# Después de la prueba, las plantas reportaron la siguiente
# producción de siete días:
#   Planta    día 1  día 2 día 3  día 4  día 5  día 6  día 7
# planta_MED   253    433   209    758    997    650    964
# planta_CAL   845    368   298    831    512    192    381
# planta_BOG   411    706   457    298    353    863    610
# planta_CUC   189    829   378    430    539    160    447
# planta_PER   484    767   145    583    409    245    613
# planta_MAN   893    377   815    559    777    295    328
# planta_GUA   794    331   395    418    742    829    773
# planta_ARM   915    433   248    706    492    240    991
# planta_BAR   208    184   918    452    486    255    564
# planta_CAR   231    302   753    546    522    264    365
#
# Se debe obtener: el día con menor producción y las unidades producidas 
# de cada planta; el día con mayor producción y las unidades producidas de 
# cada planta; el día con menor producción, las unidades producidas 
# y el nombre de la planta; el día con mayor producción, 
# las unidades producidas y el nombre de la planta; el total de producción de
# todas las plantas en los siete días y el promedio 
# de producción de éstas por día y por planta.
# La información se debe guardar en una matriz de ocho por diez (8x10) para
# posteriormente realizar el reporte solicitado.
# Después de la prueba, las plantas reportaron la siguiente
# producción de siete días:
#   Planta    día 1  día 2 día 3  día 4  día 5  día 6  día 7
# planta_MED   253    433   209    758    997    650    964
# planta_CAL   845    368   298    831    512    192    381
# planta_BOG   411    706   457    298    353    863    610
# planta_CUC   189    829   378    430    539    160    447
# planta_PER   484    767   145    583    409    245    613
# planta_MAN   893    377   815    559    777    295    328
# planta_GUA   794    331   395    418    742    829    773
# planta_ARM   915    433   248    706    492    240    991
# planta_BAR   208    184   918    452    486    255    564
# planta_CAR   231    302   753    546    522    264    365
#
# Se debe obtener: el día con menor producción y las unidades producidas 
# de cada planta; el día con mayor producción y las unidades producidas de 
# cada planta; el día con menor producción, las unidades producidas 
# y el nombre de la planta; el día con mayor producción, 
# las unidades producidas y el nombre de la planta; el total de producción de
# todas las plantas en los siete días y el promedio 
# de producción de éstas por día y por planta.
# La información se debe guardar en una matriz de ocho por diez (8x10) para
# posteriormente realizar el reporte solicitado.

# ==============================================================================
# SOLUCIÓN AL EJERCICIO DE PRODUCCIÓN DE PLANTAS (MATRIZ DE 10 PLANTA x 7 DÍAS)
# ==============================================================================

# Matriz de datos reportados por las 10 plantas durante los 7 días
# Cada fila contiene: [Nombre_Planta, Día 1, Día 2, Día 3, Día 4, Día 5, Día 6, Día 7]
MATRIZ_PRODUCCION = [
    ["planta_MED", 253, 433, 209, 758, 997, 650, 964],
    ["planta_CAL", 845, 368, 298, 831, 512, 192, 381],
    ["planta_BOG", 411, 706, 457, 298, 353, 863, 610],
    ["planta_CUC", 189, 829, 378, 430, 539, 160, 447],
    ["planta_PER", 484, 767, 145, 583, 409, 245, 613],
    ["planta_MAN", 893, 377, 815, 559, 777, 295, 328],
    ["planta_GUA", 794, 331, 395, 418, 742, 829, 773],
    ["planta_ARM", 915, 433, 248, 706, 492, 240, 991],
    ["planta_BAR", 208, 184, 918, 452, 486, 255, 564],
    ["planta_CAR", 231, 302, 753, 546, 522, 264, 365]
]


def generar_reporte(matriz):
    """
    Genera y muestra en consola el reporte completo solicitado:
    1. Día de menor y mayor producción por cada planta.
    2. Menor y mayor producción global (día, unidades y nombre de la planta).
    3. Total de producción de todas las plantas en los 7 días.
    4. Promedio de producción por planta y por día.
    """
    print("=" * 78)
    print("        REPORTE GENERAL DE PRODUCCIÓN DE PLANTAS (7 DÍAS)")
    print("=" * 78)

    # 1. Menor y mayor producción por cada planta + Promedio por planta
    print("\n1. REPORTE POR PLANTA (MENOR, MAYOR Y PROMEDIO):")
    print("-" * 78)
    print(f"{'Planta':<12} | {'Menor Prod.':<18} | {'Mayor Prod.':<18} | {'Total':<7} | {'Promedio':<8}")
    print("-" * 78)

    global_min_unidades = float("inf")
    global_min_planta = ""
    global_min_dia = 0

    global_max_unidades = float("-inf")
    global_max_planta = ""
    global_max_dia = 0

    total_general_produccion = 0

    for fila in matriz:
        planta = fila[0]
        producciones = fila[1:]  # Días 1 al 7

        # Menor por planta
        min_prod = min(producciones)
        dia_min = producciones.index(min_prod) + 1

        # Mayor por planta
        max_prod = max(producciones)
        dia_max = producciones.index(max_prod) + 1

        # Totales y promedio por planta
        total_planta = sum(producciones)
        promedio_planta = total_planta / len(producciones)
        total_general_produccion += total_planta

        # Evaluación global menor
        if min_prod < global_min_unidades:
            global_min_unidades = min_prod
            global_min_planta = planta
            global_min_dia = dia_min

        # Evaluación global mayor
        if max_prod > global_max_unidades:
            global_max_unidades = max_prod
            global_max_planta = planta
            global_max_dia = dia_max

        str_min = f"Día {dia_min} ({min_prod} un)"
        str_max = f"Día {dia_max} ({max_prod} un)"

        print(f"{planta:<12} | {str_min:<18} | {str_max:<18} | {total_planta:<7} | {promedio_planta:<8.2f}")

    print("-" * 78)

    # 2. Resultados Globales
    print("\n2. EXTREMOS GLOBALES DE PRODUCCIÓN DE TODAS LAS PLANTAS:")
    print("-" * 78)
    print(f"• MENOR producción global : {global_min_planta} -> Día {global_min_dia} con {global_min_unidades} unidades")
    print(f"• MAYOR producción global : {global_max_planta} -> Día {global_max_dia} con {global_max_unidades} unidades")

    # 3. Total General y Promedios por Día
    print("\n3. TOTALES Y PROMEDIOS GLOBALES:")
    print("-" * 78)
    print(f"• Total de producción de todas las plantas (7 días): {total_general_produccion} unidades")
    promedio_diario_todas = total_general_produccion / 7
    print(f"• Promedio general por día (todas las plantas): {promedio_diario_todas:.2f} unidades/día")

    print("\n• Promedio de producción por día (desglosado por día de la semana):")
    for col in range(1, 8):
        total_dia = sum(matriz[row][col] for row in range(len(matriz)))
        prom_dia = total_dia / len(matriz)
        print(f"   - Día {col}: Total = {total_dia} unidades | Promedio por planta = {prom_dia:.2f} unidades")

    print("=" * 78)


if __name__ == "__main__":
    generar_reporte(MATRIZ_PRODUCCION)

