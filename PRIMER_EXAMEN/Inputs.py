
"""Inputs

    Returns: Funciones de ingreso de datos int / str y array / matriz
    """

# importo funciones
from Print import *
from Validaciones import *


# seteo en el main
# FUNCION GENERAL ARRAY
def crear_array(cantidad_de_elementos:int, valor_inicial:any) -> list:
    """SE CREA UN ARRAY

    Args:
        cantidad_de_elementos (int): CANTIDAD DE ELEMENTOS
        valor_inicial (any): VALOR DE LOS ELEMENTOS

    Returns:
        list: ARRAY TERMINADO
    """
    array = [valor_inicial] * cantidad_de_elementos
    return array

# seteo en el main
# FUNCION GENERAL MATRIZ
def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    """SE CREA UNA MATRIZ

    Args:
        cantidad_filas (int): CANTRIDAD DE FILAS DE LA MATRIZ
        cantidad_columnas (int): CANTRIDAD DE COLUMNAS DE LA MATRIZ
        valor_inicial (any): VALOR DE LOS ELEMENTOS DE LA MATRIZ

    Returns:
        list: MATRIZ TERMINADA
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]    
    return matriz

# opciones
# FUNCION ESPECIFICA ENTEROS
def ingresar_opciones(primera_opcion:int, ultima_opcion:int) -> int:
    """SE INGRESA LA OPCION DEL MENU SI ES CORRECTA ENTRA DE LO CONTRARIO VUELVE A SOLICITARLA

    Args:
        primera_opcion (int): EL PRIMER VALOR DE LA OPCION
        ultima_opcion (int): EL SEGUNDO VALOR DE LA OPCION

    Returns:
        int: LA OPCION CERTIFICADA
    """
    opcion = ingresar_entero("\nINGRESE UNA OPCIÓN: ")
    while opcion > ultima_opcion or opcion < primera_opcion:
        avisar_error_opcion()
        opcion = ingresar_entero("\nINGRESE UNA OPCIÓN: ")
    return opcion

# 1 ingreso nombres                     
# FUNCION ESPECIFICA ARRAYS
def cargar_array_nombres_particiantes(array_nombres:list) -> bool:
    """SE CARGA LOS NOMBRES DE LOS 5 PARTICIPANTES EN UN ARRAY

    Args:
        array_nombres (list): EL ARRAY DONDE VAN A IR LOS NOMBRES

    Returns:
        bool: UN TRUE SI SE CARGO LA LISTA DE LO CONTRARIO QUEDA EN FALSE
    """
    for i in range(len(array_nombres)):
        #Pido el dato
        nombre = ingresar_string(f"\n    {i+1}° PARTICIPANTE: ")
        nombre = convertir_mayuscula(nombre)
        #lo corroboro el dato
        while len(nombre) < 3:
            avisar_erro_nombre()
            nombre = ingresar_string(f"\n    {i+1}° PARTICIPANTE: ")
            nombre = convertir_mayuscula(nombre)
        #Lo guardo en el array
        array_nombres[i] = nombre
    bandera_nombres_cargados = True
    return bandera_nombres_cargados

# 2 ingreso puntuaciones                     
# FUNCION ESPECIFICA MATRIZ
def cargar_matriz_puntajes(matriz_puntajes:list) -> bool:
    """SE CARGA LOS PUNTAJES DE 3 JUECES (COLUMAS) DE LOS 5 PARTICIPANTES (FILAS) EN UNA MATRIZ

    Args:
        matriz_puntajes (list): LA MATRIZ DONDE VAN A IR LOS PUNTAJES

    Returns:
        bool: UN TRUE SI SE CARGO LA MATRIZ DE LO CONTRARIO QUEDA EN FALSE
    """
    for fila in range(len(matriz_puntajes)):
        print(f"\n    {fila +1}° PARTICIPANTE")
        for columna in range(len(matriz_puntajes[0])):
            puntaje = ingresar_entero(f"      - {columna +1}° JUEZ: ")
            while puntaje > 10 or puntaje < 1:
                avisar_error_puntaje()
                print(f"\n    {fila +1}° PARTICIPANTE")
                puntaje = ingresar_entero(f"      - {columna +1}° JUEZ: ")
            matriz_puntajes[fila][columna] = puntaje 
    bandera_notas_cargadas = True
    return bandera_notas_cargadas

