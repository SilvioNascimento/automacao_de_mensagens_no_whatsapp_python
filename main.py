import pyautogui
import pandas as pd
from time import sleep

# Definindo o tempo de espera de cada ação (em segundos)
pyautogui.PAUSE = 1

# Acessando o WhatsApp no Windows
pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter")

# Tempo de espera até que o WhatsApp esteja carregado
sleep(10)

