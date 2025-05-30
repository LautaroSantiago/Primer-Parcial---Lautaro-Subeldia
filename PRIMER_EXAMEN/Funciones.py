
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
def calcular_promedio_jurado(matriz_puntajes: list, indice_jurado: int) -> float:
    """_summary_

    Args:
        matriz_puntajes (list): _description_
        indice_jurado (int): _description_

    Returns:
        float: _description_
    """
    suma = 0
    cantidad = len(matriz_puntajes)
    for i in range(cantidad):
        suma += matriz_puntajes[i][indice_jurado]
        promedio = suma / cantidad
    return promedio

def mostrar_promedio_por_jurado(matriz_puntajes: list) -> None:
    """_summary_

    Args:
        matriz_puntajes (list): _description_
    """
    cantidad_jueces = len(matriz_puntajes[0])
    for j in range(cantidad_jueces):
        promedio = calcular_promedio_jurado(matriz_puntajes, j)
        print(f"\n    {j + 1}° JURADO:")
        print(f"    + PROMEDIO: {promedio}")

# opcion 7 - jurado mas estricto
def mostrar_jurado_estricto(array_nombres: list, matriz_puntajes: list) -> float:
    """_summary_

    Args:
        array_nombres (list): _description_
        matriz_puntajes (list): _description_

    Returns:
        float: _description_
    """
    cantidad_jueces = len(matriz_puntajes[0])
    promedio_mas_bajo = calcular_promedio_jurado(matriz_puntajes, 0)
    jurado_mas_estricto = 0

    for j in range(1, cantidad_jueces):
        promedio = calcular_promedio_jurado(matriz_puntajes, j)
        if promedio < promedio_mas_bajo:
            promedio_mas_bajo = promedio
            jurado_mas_estricto = j

    print(f"\n    {jurado_mas_estricto + 1}° JUEZ:")
    print(f"    + PROMEDIO: {promedio_mas_bajo}")
    return promedio_mas_bajo

# opcion 8 - jurado mas generoso
def mostrar_jurado_generoso(array_nombres: list, matriz_puntajes: list) -> float:
    """_summary_

    Args:
        array_nombres (list): _description_
        matriz_puntajes (list): _description_

    Returns:
        float: _description_
    """
    cantidad_jueces = len(matriz_puntajes[0])
    promedio_mas_alto = calcular_promedio_jurado(matriz_puntajes, 0)
    jurado_mas_generoso = 0

    for j in range(1, cantidad_jueces):
        promedio = calcular_promedio_jurado(matriz_puntajes, j)
        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            jurado_mas_generoso = j

    print(f"\n    {jurado_mas_generoso + 1}° JUEZ:")
    print(f"    + PROMEDIO: {promedio_mas_alto}")
    return promedio_mas_alto

# opcion 9 - participantes con puntajes iguales
def mostrar_participantes_con_puntajes_iguales(array_nombres: list, matriz_puntajes: list) -> bool:
    """_summary_

    Args:
        array_nombres (list): _description_
        matriz_puntajes (list): _description_

    Returns:
        bool: _description_
    """
    bandera = False

    for i in range(len(array_nombres)):
        fila = matriz_puntajes[i]
        if len(fila) == 3 and fila[0] == fila[1] == fila[2]:
            suma = 0
            for j in range(3):
                suma += fila[j]
            promedio = suma / 3

            print(f"\n    {array_nombres[i]}")
            print("    - PUNTAJES:", fila[0], fila[1], fila[2])
            print(f"    + PROMEDIO: {promedio}")
            bandera = True

    if not bandera:
        avisar_error_participantes_con_puntajes_iguales()

    return bandera



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

