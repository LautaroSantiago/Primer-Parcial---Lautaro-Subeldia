
"""Validaciones

    Returns: Funciones para validar el ingreso de caracteres
    """

# importo funcion
from Print import *

# opciones / 2 ingreso puntajes
# FUNCION GENERAL 
# validacion de caracter entero
def ingresar_entero(mensaje:str) -> int:
    """SI EL CARACTER INGRESADO ES UN NUMERO LO CONVIERTE EN ENTERO DE LO CONTRARIO SOLICITA UN NUMERO (EN OPCIONES Y PUNTAJE)

    Args:
        mensaje (str): TEXTO QUE SOLICITA EL INGRESO DEL CARACTER

    Returns:
        int: NUMERO CONVERTIDO EN ENTERO
    """
    numero = input(mensaje)
    while not es_entero(numero):
        avisar_error_no_es_numero()
        numero = input(mensaje)
    numero = int(numero)
    return numero

# opciones / 2 ingreso puntajes
# FUNCION GENERAL 
# validacion de caracter entero
def es_entero(cadena:str) -> bool:
    """IDENTIFICA SI EL CARACTER INGRESADO ES UN NUMERO (EN OPCIONES Y PUNTAJE)

    Args:
        cadena (str): EL CARACTER INGRESADO A IDENTIFICAR

    Returns:
        bool: TRUE SI ES UN NUMERO FALSE SI NO LO ES
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False 
    return retorno

# 1 ingreso nombres
# FUNCION GENERAL 
# validacion de caracter string
def ingresar_string(mensaje:str) -> str:
    """SI EL CARACTER INGRESADO PARA LOS NOMBRE ES UN STRING LO ENVIA DE LO CONTRARIO SOLICITA UN STRING

    Args:
        mensaje (str): TEXTO QUE SOLICITA EL INGRESO DE UN STRING

    Returns:
        str: EL STRING ANALIZADO
    """
    letra = input(mensaje)
    while not es_alfabetico(letra):
        avisar_erro_nombre()
        letra = input(mensaje)
    return letra

# 1 ingreso nombres
# FUNCION GENERAL 
# validacion de caracter string
def es_alfabetico(cadena:str) -> bool:
    """IDENTIFICA SI EL CARACTER INGRESADO PARA LOS NOMBRE  ES UN STRING

    Args:
        cadena (str): EL CARACTER INGRESADO A IDENTIFICAR

    Returns:
        bool: TRUE SI ES UN STRING FALSE SI NO LO ES
    """
    if len(cadena) >= 3:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if (valor_ascii > 90 or valor_ascii < 65) and (valor_ascii > 122 or valor_ascii < 97):
                retorno = False
                break
    else:
        retorno = False 
    return retorno

# 1 ingreso nombres
# FUNCION GENERAL 
# convertir todos los caracteres string a mayuscula
def convertir_mayuscula(cadena:str) -> str:
    """CONVIERTE LOS NOMBRES INGRESADOS EN MAYUSCULA

    Args:
        cadena (str): EL STRING A CONVERTIR EN MAYUSCULA

    Returns:
        str: EL STRING EN MAYUSCULA
    """
    cadena_aux = ""
    for i in range(len(cadena)):
        valor_ascii = ord(cadena[i])
        if valor_ascii >= 97 and valor_ascii <= 122:
            mayuscula = chr(valor_ascii - 32)
            cadena_aux += mayuscula
        else:
            cadena_aux += cadena[i]
    return cadena_aux

