# -*- coding: 850 -*-

# import pandas as pd


def response(input_message):
    message = input_message.lower()

    # datos = pd.read_csv('RENDIMIENTO.csv')
    # df = pd.DataFrame[datos]

    if message == "1":
        return "Ver Rendimientos: http://www.donricardo.com/"
        # if message == "71852207":
        # return 'Hola Jossip Jair, su rendimiento es 100 cjs'
        # elif message == "11111111":
        # return 'Hola Pepito, su rendimiento de la semana es:\n10/05 = 570pun\n 11/05 = 800pun'
        # else:
        # return "No se encuentra rendimiento, favor de escribir un DNI valido"
    elif message == "2":
        return "Ver Politica Salarial: http://www.donricardo.com/politicasalarial/"
    elif message == "3":
        return "Descarga la APP Don Ricardo para visualizar tus boletas: " \
               "https://play.google.com/store/apps/details?id=pe.yapu.workapp&hl=es"
    elif message == "4":
        return "Conoce mas de Nosotros: http://donricardo.com/nosotros/"
    else:
        return '­Hola soy R2D2! ¨Deseas saber mas de nosotros? ­Te puedo ayudar! ' \
               'Ingresa una de las siguientes opciones para mayor informacion: \n1. *Ver rendimientos*\n2. *Ver ' \
               'politica salarial*\n3. *Descargar App Don Ricardo*\n4. *Nosotros*'
