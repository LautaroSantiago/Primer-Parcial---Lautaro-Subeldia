
"""Funciones

    Returns: Funciones operativas
    """

# importo funciones
from Print import *
from Inputs import *
from Validaciones import convertir_mayuscula


# opcion 3 - todas las puntuaciones y promedios
def mostrar_un_solo_participante(matriz_puntajes:list, indice:int) -> None:
    """MUESTRA UN SOLO PUNTAJE

    Args:
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES
        indice (int): IDICE DEL PUNTAJE
    """
    for j in range(len(matriz_puntajes[indice])):
        print(f"    - PUNTAJE {j + 1}° JUEZ: {matriz_puntajes[indice][j]}")

def mostrar_todos_los_participantes(array_nombres: list, matriz_puntajes: list) -> None:
    """MUESTRA TODOS LOS PARTICIPANTES

    Args:
        array_nombres (list): ARRAY CON NOMBRES
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES
    """
    for i in range(len(array_nombres)):
        nombre = array_nombres[i]
        promiedio = promediar_participante(matriz_puntajes, i)
        print(f"    NOMBRE DEL PARTICIPANTE: {nombre}")
        mostrar_un_solo_participante(matriz_puntajes, i)
        print(f"    + PROMEDIO: {promiedio}\n")
        
def sumar_notas_participante(matriz_puntajes: list, indice_participante: int) -> int:
    """SUMA LA NOTAS DEL PARTICIPANTE

    Args:
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES
        indice_participante (int): IDICE DEL PARTICIPANTE

    Returns:
        int: SUMA DE PUNTAJE
    """
    suma = 0
    for nota in matriz_puntajes[indice_participante]:
        if type(nota) == int or type(nota) == float:
            suma += nota
    return suma

def promediar_participante(matriz_puntajes: list, indice_participante: int) -> float:
    """SACA EL PROMEDIO DEL PUNTAJE DEL PARTICIPANTE

    Args:
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES
        indice_participante (int): INDICE DEL PARTICIPANTE

    Returns:
        float: EL PROMEDIO DEL PUNTAJE
    """
    suma = sumar_notas_participante(matriz_puntajes, indice_participante)
    cantidad_notas = len(matriz_puntajes[indice_participante])
    promedio = 0
    if cantidad_notas > 0:
        promedio = suma / cantidad_notas
        return promedio
    else:
        return promedio
    
# opcion 4 - puntuaciones y promedios menor a 4
# opcion 5 - puntuaciones y promedios menor a 8
def mostrar_promedio_menor(array_nombres:list, matriz_puntajes:list, minimo:float) -> bool:
    """MUESTRA LOS PROMEDIOS MAS CHICO QUE SE LE INDIQUE (4 / 8)

    Args:
        array_nombres (list): ARRAY DE LOS NOMBRES
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES
        minimo (float): PUNTAJE MINIMO FILTRO SETEABLE
    
    Returns:
    bool: TRUE SI EXISTE EL PROMEDIO MENOR FALSE QUE NO
    """
    bandera_menor = False
    for fila in range(len(array_nombres)):
        suma = 0
        for columna in range(len(matriz_puntajes[fila])):
            suma += matriz_puntajes[fila][columna]
        promedio = suma / len(matriz_puntajes[fila])
        if promedio < minimo:
            print(f"\n    NOMBRE DEL PARTICIPANTE: {array_nombres[fila]}")
            print(f"    + PROMEDIO: {promedio}")
            bandera_menor = True
    if bandera_menor == False:
        avisar_error_promedio_menor(minimo)
    return bandera_menor

# opcion 6 - promedio de cada jurado        
def mostrar_promedio_por_jurado(matriz_puntajes: list) -> int | float:
    """MUESTRA EL PROMEDIO DE ACUERDO AL JURADO

    Args:
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES

    Returns:
        int | float: EL PROMEDIO DE LOS PUNTAJES OTORGADOS
    """
    promedio = 0
    cantidad_jueces = len(matriz_puntajes[0])        # columnas
    cantidad_participantes = len(matriz_puntajes)    # filas
    for juez in range(cantidad_jueces):
        suma = 0
        for participante in range(cantidad_participantes):
            suma += matriz_puntajes[participante][juez]
        promedio = suma / cantidad_participantes
        print(f"\n    {juez +1}° JURADO:")         
        print(f"    + PROMEDIO: {promedio:}")
    return promedio
        
# opcion 7 - jurado mas estricto
def mostrar_jurado_estricto(array_nombres: list, matriz_puntajes: list) -> float:
    """MUESTRA EL JURADO QUE PONE NOTAS MAS BAJAS

    Args:
        array_nombres (list): ARRAY DE NOMBRES
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES

    Returns:
        float: PROMEDIO DEL JURADO QUE MENOS PUNTUA
    """
    bandera_Primero = False
    promedio_bajo = 0
    jurado_bajo = 0
    cantidad_jurados = len(matriz_puntajes[0])  # cantidad de columnas
    cantidad_concursantes = len(matriz_puntajes)
    for jurado in range(cantidad_jurados):  # recorremos por jurado (columna)
        suma = 0
        for concursante in range(cantidad_concursantes):  # recorremos filas
            suma += matriz_puntajes[concursante][jurado]
        promedio = suma / cantidad_concursantes
        if bandera_Primero == False or promedio < promedio_bajo:
            bandera_Primero = True
            promedio_bajo = promedio
            jurado_bajo = jurado  # índice, no le sumamos 1 todavía
    print(f"\n    {jurado_bajo + 1}° JUEZ:")         
    print(f"    + PROMEDIO: {promedio_bajo}")
    return promedio
    
# opcion 8 - jurado mas generoso
def mostrar_jurado_generoso(array_nombres: list, matriz_puntajes: list) -> float:
    """MUESTRA EL JURADO QUE PONE NOTAS MAS ALTAS

    Args:
        array_nombres (list): ARRAY DE LOS NOMBRES
        matriz_puntajes (list): MATRIZ DE LOS PUNTAJES

    Returns:
        float: PROMEDIO DEL JURADO QUE MAS PUNTUA
    """
    bandera_Primero = False
    promedio_alto = 0
    jurado_alto = 0
    cantidad_jurados = len(matriz_puntajes[0])  # cantidad de columnas
    cantidad_concursantes = len(matriz_puntajes)
    for jurado in range(cantidad_jurados):  # recorremos por jurado (columna)
        suma = 0
        for concursante in range(cantidad_concursantes):  # recorremos filas
            suma += matriz_puntajes[concursante][jurado]
        promedio = suma / cantidad_concursantes
        if bandera_Primero == False or promedio > promedio_alto:
            bandera_Primero = True
            promedio_alto = promedio
            jurado_alto = jurado  # índice, no le sumamos 1 todavía
    print(f"\n    {jurado_alto + 1}° JUEZ:")         
    print(f"    + PROMEDIO: {promedio_alto}")
    return promedio 
           
# opcion 9 - participantes con puntajes iguales
def mostrar_participantes_con_puntajes_iguales(array_nombres: list, matriz_puntajes: list) -> bool:
    """MUESTRA LOS PARTICIPANTES CON PUNTAJES IGUALES ENTRE LOS 3 JUECES

    Args:
        array_nombres (list): ARRAY DE NOMBRES
        matriz_puntajes (list): MATRIZ DE PUNTAJES

    Returns:
        bool: SI ENCUENTRA COINCIDENCIAS ENVIA TRUE DE LO CONTRARIO FALSE
    """
    bandera_encontrado = False
    limite = min(len(array_nombres), len(matriz_puntajes))
    for i in range(limite):
        fila = matriz_puntajes[i]
        if len(fila) == 0:
            continue
        # Verificar si los tres puntajes son exactamente iguales
        if fila[0] == fila[1] == fila[2]:
            promedio = promediar_participante(matriz_puntajes, i)

            print(f"\n    {array_nombres[i]}")
            print("    - PUNTAJES:", end = " ")
            for nota in fila:
                print(nota, end=" ")
            print(f"\n    + PROMEDIO: {promedio}")
            bandera_encontrado = True
    if not bandera_encontrado:
        avisar_error_participantes_con_puntajes_iguales()
    return bandera_encontrado


# opcion 10 - buscando participantes por nombre
def buscar_participante(array_nombres: list, matriz_puntajes: list) -> bool:
    """BUSCA COINCIDENCIAS ENTRE LOS NOMBRES

    Args:
        array_nombres (list): ARRAY DE NOMBRES
        matriz_puntajes (list): MATRIZ DE PUNTAJES

    Returns:
        bool: TRUE SI SE ENCUENTRA COINCIDENCIAS FALSE SI NO
    """
    nombre_ingresado = convertir_mayuscula(input("     INGRESE EL NOMBRE DEL PARTICIPANTE: "))
    bandera_encontrado = False
    for i, nombre_actual in enumerate(array_nombres):
        if convertir_mayuscula(nombre_actual) == nombre_ingresado:
            bandera_encontrado = True
            print(f"\n     PARTICIPANTE ENCONTRADO:")
            print(f"     - NOMBRE: {array_nombres[i]}")
            print(f"     - PUNTAJES:")
            for j, puntaje in enumerate(matriz_puntajes[i]):
                print(f"     - JUEZ {j +1}: {puntaje}")
            promedio = sum(matriz_puntajes[i]) / len(matriz_puntajes[i])
            print(f"     + PROMEDIO: {promedio}")
            break
    if not bandera_encontrado:
        avisar_error_buscar_participante()
    return bandera_encontrado
        
# opcion 11 - orden alfabetico de participanres
def intercambiar_indices(array:list, izq:int, der:int) -> int:
    """INTERCAMBIA INDICES DE IZQUIERDA DERECHA

    Args:
        array (list): LISTA DE NOMBRES
        izq (int): POSICION IZQUIEDA EN EL ARRAY
        der (int): POSICION DERECHA EN EL ARRAY

    Returns:
        int: IZQUIERDA
    """
    aux_izq = array[izq]
    array[izq] = array[der]
    array[der] = aux_izq
    return izq     
        
def mostrar_orden_alfabetico(array_nombres:list, matriz_puntajes:list) -> int:
    """ORDENA ALFABETICAMENTE POR EL MÉTODO DEL BURBUJEO

    Args:
        array_nombres (list): ARRAY DE NOMBRES
        matriz_puntajes (list): MATRIZ DE PUNTAJES

    Returns:
        int: IZQUIERDA
    """
    for izq in range(len(array_nombres) - 1):
        for der in range(izq + 1, len(array_nombres)):
        # Comparacion
            if array_nombres[izq] > array_nombres[der]:
            # Swap
                intercambiar_indices(array_nombres, izq, der)
                intercambiar_indices(matriz_puntajes, izq, der)
    return izq

