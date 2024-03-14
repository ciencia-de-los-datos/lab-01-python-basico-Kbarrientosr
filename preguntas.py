"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def lect_doc():
    data_base = "data.csv"
    with open(data_base, "r") as file:
        list_base = file.readlines()

    list_base = [i.replace("\n","") for i in list_base]
    list_base = [i.split("\t") for i in list_base]

    return list_base

lect_doc()

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    list_base = lect_doc()

    sum_sec_col = 0
    list_sec_col = []

    for lista_interna in list_base:
        list_sec_col.append(int(lista_interna[1]))

    sum_sec_col = sum(i for i in list_sec_col)
    return sum_sec_col

respuesta=pregunta_01()

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    list_base = lect_doc()

    list_preg_2=[]
    dicc_preg_2={}

# #sacamos los datos de la columna 0 le sumamos 1 y se convierte en tupla.
# #luego las organizamos alfabeticamente posicionandonos en la clave key
    for i in list_base:
        list_preg_2.append((i[0],1))
        list_preg_2= sorted(list_preg_2, key=lambda x:x[0])

# #se hace esto para evitar errores en caso de que no encuentre la llave
# #y al final con el append traemos los valores de cada clave
    for key, value in list_preg_2:
        if key not in dicc_preg_2.keys():
            dicc_preg_2[key] = []
        dicc_preg_2[key].append(value)

# # dicc_preg_2

    Resp_seg_eje=[]      
    for key, value in dicc_preg_2.items():
       Resp_seg_eje.append((key, sum(value)))

    return Resp_seg_eje

respuesta = pregunta_02()


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    list_base = lect_doc()

    #primero creamos lista y diccionario
    list_preg_3=[]
    dicc_preg_3={}

#creamos lista con la letra de la columna 0 y convertirmos en entero la columna
#1 para extraer el valor de cada letra correspondiente
#organizamos alfabeticamente
    for i in list_base:
        list_preg_3.append((i[0], int(i[1])))
        list_preg_3= sorted(list_preg_3, key=lambda x:x[0])

#se hace esto para evitar errores en caso de que no encuentre la llave
#y al final con el append traemos los valores de cada clave
    for key, value in list_preg_3:
        if key not in dicc_preg_3.keys():
            dicc_preg_3[key] = []
        dicc_preg_3[key].append(value)

#append se encarga de adicionar
        
    Resp_ter_eje = []

    for key, value in dicc_preg_3.items():
       Resp_ter_eje.append((key, sum(value)))

    
    return Resp_ter_eje
respuesta=pregunta_03()

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    list_base = lect_doc()

    list_month_4=[]

    list_base[0:] = [i + [i[2].split("-")[1]] for i in list_base[0:]]

    list_preg_4=[]
    dicc_preg_4={}

    for i in list_base:
        list_preg_4.append((i[5],1))
        list_preg_4 = sorted(list_preg_4, key=lambda x: x[0])

    for key, value in list_preg_4:
        if key not in dicc_preg_4.keys():
            dicc_preg_4[key] = []
        dicc_preg_4[key].append(value)

    Resp_cuar_eje = []

    for key, value in dicc_preg_4.items():
        Resp_cuar_eje.append((key, sum(value)))

    return Resp_cuar_eje

respuesta=pregunta_04()

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    list_base = lect_doc()

    list_preg_5 = []
    dicc_preg_5 = {}

    for i in list_base:
        list_preg_5.append((i[0], int(i[1])))
        list_preg_5 = sorted(list_preg_5, key = lambda x: x[0])


    for key, value in list_preg_5:
        if key not in dicc_preg_5.keys():
            dicc_preg_5[key] = []
        dicc_preg_5[key].append(value)

    Resp_quin_eje = []

    for key,value in dicc_preg_5.items():
        Resp_quin_eje.append((key, max(value), min(value)))

    return Resp_quin_eje

respuesta=pregunta_05()


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    list_base = lect_doc()
    data_base = list_base
    list_base2 = [i[4].split(",") for i in list_base[0:]]

    list_preg_3 = []
    dicc_preg_6 = {}

    for i in list_base2:
        for j in i:
            list_preg_2 = tuple(j.split(":"))
            list_preg_3.append(list_preg_2)

    list_preg_3 = sorted(list_preg_3, key = lambda x: x[0])

    for key,value in list_preg_3:
        if key not in dicc_preg_6.keys():
            dicc_preg_6[key] = []
        dicc_preg_6[key].append(int(value))

    Resp_sext_eje = []

    for key,value in dicc_preg_6.items():
        Resp_sext_eje.append((key,min(value), max(value)))

    return Resp_sext_eje

respuesta=pregunta_06()



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    list_base = lect_doc()

    data_base = list_base

    list_preg_7 = []
    dicc_preg_7 = {}

    for i in list_base:
        list_preg_7.append((int(i[1]), i[0]))
        list_preg_7 = sorted(list_preg_7, key=lambda x: x[0])

    for key,value in list_preg_7:
        if key not in dicc_preg_7.keys():
            dicc_preg_7 [key] = []
        dicc_preg_7[key].append(value)

    Resp_sept_eje = []

    for key, value in dicc_preg_7.items():
        Resp_sept_eje.append((key,value))

    return Resp_sept_eje

respuesta=pregunta_07()

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    list_base = lect_doc()

    list_preg_8 = []
    dicc_preg_8= {}

    for i in list_base:
        list_preg_8.append((int(i[1]), i[0]))
        list_preg_8 = sorted(list_preg_8, key=lambda x: x[1])
        list_preg_8 = sorted(list_preg_8, key=lambda x: x[0])

    for key, value in list_preg_8:
        if key not in dicc_preg_8.keys():
            dicc_preg_8 [key] = []
        dicc_preg_8[key].append(value)

    Resp_oct_eje = []

    for key,value in dicc_preg_8.items():
        value = list(set(value))
        values = "".join(value)
        values = sorted(values)
        Resp_oct_eje.append((key,values))

    return Resp_oct_eje

respuesta=pregunta_08()

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    list_base = lect_doc()

    data_base = list_base
    list_base2 = [i[4].split(",") for i in list_base[0:]]

    list_preg_3 = []
    dicc_preg_9 = {}

    for i in list_base2:
        for j in i:
            list_preg_2 = tuple (j.split(":"))
            list_preg_3.append(list_preg_2)

    list_preg_3 = sorted(list_preg_3, key=lambda x: x[0])

    for key,value in list_preg_3:
        if key not in dicc_preg_9.keys():
            dicc_preg_9[key] = []
        dicc_preg_9[key].append((len,value))

    list_preg_9  = []

    for key, value in dicc_preg_9.items():
        list_preg_92 = len(value)
        list_preg_9.append((key, list_preg_92))

    Resp_nov_eje = {key:value for key,value in list_preg_9 }
  
    return Resp_nov_eje

respuesta=pregunta_09()

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    list_base = lect_doc()

    data_base = list_base

    Resp_dec_eje = []

    for i in list_base:
        Resp_dec_eje.append((i[0],len(i[3].split(",")),len(i[4].split(","))))


    return Resp_dec_eje

respuesta=pregunta_10()

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    list_base = lect_doc()

    list_preg_11 = []
    dicc_preg_11 = {}

    for i in list_base:
        list_preg_11.append((i[3].split(","),int(i[1])))
    
    list_tupla2 = []

    for key, value in list_preg_11:
        for i in key:
            list_tupla2.append((i,value))
    
    list_tupla2 = sorted(list_tupla2, key=lambda x: x[0])

    for key, value in list_tupla2:
        if key not in dicc_preg_11.keys():
            dicc_preg_11[key] = []
        dicc_preg_11[key].append((value))

    list_prueba = []
    Resp_onc_eje = {}

    for key, value in dicc_preg_11.items():
        list_prueba.append((key,sum(value)))

    Resp_onc_eje = {key:value for key, value in list_prueba}

    return Resp_onc_eje

respuesta = pregunta_11()



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    list_base = lect_doc()

    list_preg_12 = []
    dicc_preg_12 = {}

    for i in list_base:
        list_preg_12.append((i[0], i[4].split(",")))
    
    list_tupla12 = []
    list_tupla13 = []

    for key, value in list_preg_12:        
        for i in value:
            list_tupla12.append((key, i.split(":")))
            
    for key, value in list_tupla12:
        list_tupla13.append((key, int(value[1])))

    list_tupla13 = sorted(list_tupla13, key=lambda x: x[0])

    for key, value in list_tupla13:
        if key not in dicc_preg_12.keys():
            dicc_preg_12[key] = []
        dicc_preg_12[key].append(value)
        
    list_Prob12 = []

    for key, value in dicc_preg_12.items():
            list_Prob12.append((key, sum(value)))

    Resp_doc_eje = {key:value for key, value in list_Prob12}

    return Resp_doc_eje 

respuesta = pregunta_12()

