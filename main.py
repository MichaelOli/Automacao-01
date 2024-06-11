#Importando Biblioteca
import pyautogui as auto
import time

#Abre menu inicar do windows
auto.press('win')
time.sleep()
#Abre o Chrome
auto.write('chrome')
time.sleep(3)
auto.press('enter')
time.sleep(2)
# Maximizar tela
auto.hotkey('alt', 'space',)
auto.press('x')
time.sleep(5)
auto.write('github.com')
auto.press('enter')

#abre o classroom em uma nova guia
auto.hotkey('ctrl','t')
auto.write('classroom.google.com')
auto.press('enter')


