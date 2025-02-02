# Drescriotion: This is a bot automation for slow songs the Guitar Flash game with python code
# Descrição: Este é um bot de automação para músicas lentas do jogo Guitar Flash com código python

# Import the necessary libraries
# Importe as bibliotecas necessárias
import pyautogui
import keyboard
from time import sleep
# loop to run the code until the key 1 is pressed
# loop para executar o código até que a tecla 1 seja pressionada
while keyboard.is_pressed('1') == False:
    # Check button with corresponding color on the screen
    # Verifique o botão com a cor correspondente na tela
    if pyautogui.pixelMatchesColor(X, Y, (R, G, B)) #coordinates and color
        pyautogui.press('corresponding color button ') # press button key
        sleep(0.05)
    if pyautogui.pixelMatchesColor(X, Y, (R, G, B)) #coordinates and color
        pyautogui.press('corresponding color button') # press button key
        sleep(0.05)
    #repeat the same for all the buttons
    # repita o mesmo para todos os botões
