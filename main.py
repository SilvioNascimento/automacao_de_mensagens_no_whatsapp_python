import pyautogui
from Temporizador import iniciar_contagem
import pyperclip
from time import sleep

# A lista de contatos
lista_contatos = ["Meu Numero", "Base de teste", "Família Nascimento", "Teste 1", "Teste 2", "Teste 3"]

# A mensagem que será usado para ser enviado para os contatos
mensagem = """Fala galera, beleza?
Isso aqui é só uma mensagem teste, não precisa se preocupar.
Desculpa pelo incômodo e obrigado pela compreensão. ❤
"""

# Copiando a mensagem
pyperclip.copy(mensagem)

# Definindo o tempo de espera de cada ação (em segundos)
pyautogui.PAUSE = 1

# Acessando o WhatsApp no Windows
pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter")

# Tempo de espera até que o WhatsApp esteja carregado
iniciar_contagem(5)

# mandando mensagem para o primeiro contato
pyautogui.click(x=215, y=119)
pyautogui.write(str(lista_contatos[0]))

del lista_contatos[0]   # Eliminando o primeiro contato, já que iremos mandar a mensagem nele primeiro

pyautogui.press("enter")
iniciar_contagem(5)
pyautogui.click(x=553, y=701)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Enviando a mesma mensagem para os demais contatos.
pyautogui.click(x=1076, y=621, button="right")

sleep(1)
pyautogui.doubleClick(x=1155, y=312)

pyautogui.PAUSE = 2
for index, contato in enumerate(lista_contatos):
    pyautogui.write(str(contato))
    if index == 0:
        pyautogui.press("tab")
        pyautogui.press("enter")
        continue
    
    pyautogui.press("tab", presses=2, interval=1)
    pyautogui.press("enter")
    
pyautogui.press("tab")
pyautogui.press("enter")