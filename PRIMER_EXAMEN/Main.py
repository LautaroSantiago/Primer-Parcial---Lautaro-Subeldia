
#Main donde se hacen las llamadas y ejecuta el programa

# importo funciones
import os # importo funciones permite usar el cls y borrar inputs en consola
from Inputs import *  
from Print import * 
from Funciones import *

# inicializo banderas para mostrar y entrar a opciones del menu
bandera_nombres_cargados = False
bandera_notas_cargadas = False

# creo e incicializo array y matriz 
array_nombres = crear_array(5, "") # 5 nombres (participantes)
matriz_puntajes = crear_matriz(5, 3, 0)  # 5 filas (participantes), 3 columnas (jurados)

# menu siempre funciona hasta la opcion de brake
while True:
    mostrar_menu(bandera_nombres_cargados, bandera_notas_cargadas)

    # tomo la opcion y marco la minima y maxima opcion
    opcion = ingresar_opciones(1,12)
    
    if opcion == 1:
        mostrar_mensaje_menu("\n1 - INGRESANDO NOMBRES DE PARTICIPANTES")
        bandera_nombres_cargados = cargar_array_nombres_particiantes(array_nombres)
    elif opcion == 2:
        if bandera_nombres_cargados == True:
            mostrar_mensaje_menu("\n2 - INGRESANDO PUNTUACIONES DE PARTICIPANTES (entre 1 - 10)")
            bandera_notas_cargadas = cargar_matriz_puntajes(matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 3:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n3 - TODAS LAS PUNTUACIONES Y PROMEDIOS\n")
            mostrar_todos_los_participantes(array_nombres, matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 4:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n4 - PUNTUACIONES Y PROMEDIOS MENOR A 4")
            mostrar_promedio_menor(array_nombres, matriz_puntajes, 4)
        else:
            avisar_error()
    elif opcion == 5:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n5 - PUNTUACIONES Y PROMEDIOS MENOR A 8\n")
            mostrar_promedio_menor(array_nombres, matriz_puntajes, 8)
        else:
            avisar_error()        
    elif opcion == 6:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n6 - PROMEDIO DE CADA JURADO")
            mostrar_promedio_por_jurado(matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 7:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n7 - JURADO MAS ESTRICTO")
            mostrar_jurado_estricto(array_nombres, matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 8:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n8 - JURADO MAS GENEROSO")
            mostrar_jurado_generoso(array_nombres, matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 9:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n9 - PARTICIPANTES CON PUNTAJES IGUALES",)
            mostrar_participantes_con_puntajes_iguales(array_nombres, matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 10:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n10 - BUSCANDO PARTICIPANTES POR NOMBRE")
            buscar_participante(array_nombres, matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 11:
        if bandera_nombres_cargados == True and bandera_notas_cargadas == True:
            mostrar_mensaje_menu("\n11 - ORDEN ALFABÉTICO DE PARTICIPANTES\n")
            mostrar_orden_alfabetico(array_nombres, matriz_puntajes)
            mostrar_todos_los_participantes(array_nombres, matriz_puntajes)
        else:
            avisar_error()
    elif opcion == 12:
        mostrar_mensaje_menu("\nSALIENDO DEL SISTEMA...\n")
        break

    input("\nPRESIONE ENTER PARA CONTINUAR... ")
    os.system("cls")

