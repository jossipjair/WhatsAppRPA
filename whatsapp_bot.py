# -*- coding: 850 -*-

import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response

# Inicializa Mouse Clic
mouse = Controller()


# Instrucciones para bot whatsapp
class Whatsapp:

    # Define valores iniciales
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navegar en busqueda de nuevos mensajes (punto verde)
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    # Navegar al input box del mensaje
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paper_clic.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(110, 20, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)

    # Navegar hacia el mensaje para realizar operacion de copiado
    def nav_message(self):
        try:
            position = pt.locateOnScreen('paper_clic.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(90, -50, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message): ', e)

    # Copiar el mensaje para procesarlo
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(50, -100, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.message = pc.paste()
        print('Enviado por usuario: ', self.message)

    # Enviar mensaje a usuarios
    def send_message(self):
        try:
            # Comprobar si el ultimo mensaje fue el mismo que el que acabamos de enviar (para evitar enviar el mismo
            # mensaje)
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('Se ha respondido: ', bot_response)
                pt.typewrite(bot_response, interval=.05)
                pt.typewrite('\n')
                # Asignar al mensaje que acabamos de copiar
                self.last_message = self.message
            else:
                print('No hay mensajes nuevos')
        except Exception as e:
            print('Exception (send_message): ', e)

    # Cerrar caja de respueta del mensaje
    def nav_x(self):
        try:
            position = pt.locateOnScreen('x.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(15, 10, duration=self.speed)
            mouse.click(Button.left, 1)
        except Exception as e:
            print('Exception (nav_x): ', e)


# Inicializa bot
wa_bot = Whatsapp(speed=.5, click_speed=.4)

# Correo el script con un bucle infinito
while True:
    sleep(2)
    wa_bot.nav_green_dot()
    wa_bot.nav_x()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()

    # Tiempo de espera para busqueda de nuevos mensajes
    sleep(5)
