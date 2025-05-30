
"""Print: Funciones que solo imprimen menu y alertas"""

# FUNCION ESPECIFICA
def mostrar_menu(bandera_nombres_cargados:bool, bandera_notas_cargadas:bool) -> None:
    """MUESTRA UN MENU DE OPCIONES

    Args:
        bandera_nombres_cargados (bool): ES EL OK DE QUE SE HAN INGRESADO LOS NOMBRES
        bandera_notas_cargadas (bool): ES EL OK DE QUE SE HAN INGRESADO LAS NOTAS
    """
    print("\n████████████████████ MENÚ PRINCIPAL ███████████████████████")
    if bandera_nombres_cargados == False:
        print("( 1 )  -> CARGAR NOMBRE DE PARTICIPANTES ")
    if bandera_nombres_cargados == True and bandera_notas_cargadas == False:
        print("( 1 )  -> MODIFICAR NOMBRE DE PARTICIPANTES ")
        print("( 2 )  -> CARGAR PUNTUACIONES DE PARTICIPANTES ")
    if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
        print("( 1 )  -> MODIFICAR NOMBRE DE PARTICIPANTES ")
        print("( 2 )  -> MODIFICAR PUNTUACIONES DE PARTICIPANTES ")
        print("\n( 3 )  -> PUNTUACIONES Y PROMEDIO ")
        print("( 4 )  -> PARTICIPANTES CON PROMEDIO MENOR A 4 ")
        print("( 5 )  -> PARTICIPANTES CON PROMEDIO MENOR A 8 ")
        print("( 6 )  -> PROMEDIO DE CADA JURADO ")
        print("( 7 )  -> JURADO MÁS ESTRICTO ")
        print("( 8 )  -> JURADO MÁS GENEROSO ")
        print("( 9 )  -> PARTICIPANTES CON PUNTUACIONES IGUALES ")
        print("\n( 10 ) -> BUSCAR PARTICIPANTE POR NOMBRE ")
        print("\n( 11 ) -> ORDENAR ALFABETICAMENTE NOMBRES")
    print("\n( 12 ) << SALIR >>")

# FUNCION ESPECIFICA
def mostrar_mensaje_menu(mensaje:str) -> None:
    """MUESTRA EL MENSAJE DE LA OPCION INTRODUCIDA

    Args:
        mensaje (str): LA OPCION
    """
    print("\n███████████████████████████████████████████████████████████")
    print(mensaje)

# FUNCION ESPECIFICA
def avisar_error() -> None:
    """AVISO DE ERROR PO FALTA DE INGRESO DE NOMBRES Y PUNTUACIONES
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|████████¡ERROR!█████████|")
    print("|████PRIMERO INGRESE█████|")
    print("|███████LOS NOMBRES██████|")
    print("|███Y LAS PUNTUACIONES███|")
    print("|████████████████████████|\n")

# FUNCION ESPECIFICA
def avisar_error_opcion() -> None:
    """AVISO DE ERROR POR MARCAR UNA OPCION DISTINTA A LA DEL MENU
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|████████¡ERROR!█████████|")
    print("|██OPCIÓN ENTRE 1 Y 12███|")
    print("|████████████████████████|\n")

# FUNCION ESPECIFICA
def avisar_error_no_es_numero() -> None:
    """AVISO DE ERROR PORQUE NO SE INGRESO UN NUMERO
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|████████¡ERROR!█████████|")
    print("|████NO ES UN NÚMERO█████|")
    print("|████████████████████████|\n")

# FUNCION ESPECIFICA
def avisar_erro_nombre() -> None:
    """AVISO DE ERROR PORQUE EL NOMBRE NO CUMPLE CON LAS CONDICIONES
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|████████¡ERROR!█████████|")
    print("|████ NOMBRE INVÁLIDO████|")
    print("|████████████████████████|")
    print("|██- AL MENOS 3 LETRAS███|")
    print("|██- NO SER UN NÚMERO████|")
    print("|████████████████████████|\n")

# FUNCION ESPECIFICA
def avisar_error_puntaje() -> None:
    """AVISO DE ERROR PORQUE EL PUNTAJE NO ESTA EN EL RANGO ESTIPULADO
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|████████¡ERROR!█████████|")
    print("|████PUNTAJE INVÁLIDO████|")
    print("|████████████████████████|")
    print("|█████(ENTRE 1 Y 10)█████|")
    print("|████████████████████████|\n")
    
# FUNCION ESPECIFICA
def avisar_error_promedio_menor(minimo:int) -> None:
    """AVISO PORQUE NO HAY UN PROMEDIO MENOR AL VALOR ESTIPULADO

    Args:
        minimo (int): VALOR MINIMO ESTIPULADO
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|██NO HAY PARTICIPANTES██|")
    print("|██CON PROMEDIO MENOR A██|")
    print(f"|███████████{minimo}████████████|")
    print("|████████████████████████|\n")

# FUNCION ESPECIFICA    
def avisar_error_participantes_con_puntajes_iguales() -> None:
    """AVISO PORQUE NO HAY PARTICIPANTES CON NOTAS IGUALES
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|██NO HAY PARTICIPANTES██|")
    print("|██CON PUNTAJES IGUALES██|")
    print("|████████████████████████|\n")

# FUNCION ESPECIFICA    
def avisar_error_buscar_participante() -> None:
    """AVISO PORQUE NO EXISTE COINCIDENCIAS DEL NOMBRE CON LOS PARTICIPANTES
    """
    print("\n__________________________")
    print("|████████████████████████|")
    print("|████PARTICIPANTE NO█████|")
    print("|███████ENCONTRADO███████|")
    print("|████████████████████████|\n")
    
    