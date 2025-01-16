import pyautogui
from time import sleep
from Temporizador import iniciar_contagem

# Definindo o tempo de espera de cada ação (em segundos)
pyautogui.PAUSE = 1

# Acessando o WhatsApp no Windows
pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter")

# Tempo de espera até que o WhatsApp esteja carregado
iniciar_contagem(5)

