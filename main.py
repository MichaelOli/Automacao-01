#Importando Biblioteca
import pyautogui as auto
import time
#Define espera para cada comando
auto.PAUSE = 1.5
#Abre menu inicar do windows
auto.press('win')

#Abre o Chrome
auto.write('chrome')

auto.press('enter')

# Maximizar tela
auto.hotkey('alt', 'space',)
auto.press('x')
auto.write('github.com')
auto.press('enter')

#abre o classroom em uma nova guia
auto.hotkey('ctrl','t')
auto.write('classroom.google.com')
auto.press('enter')


