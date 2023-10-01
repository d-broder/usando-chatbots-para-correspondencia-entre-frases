import time

import pyautogui as pya
import pyperclip


def texto_copiado_pyautogui(x_inicio, y_inicio, x_final, y_final):
    pyperclip.copy("a")
    pya.moveTo(x_inicio, y_inicio, duration=0.1)
    pya.mouseDown()
    pya.moveTo(x_final, y_final, duration=0.1)
    pya.mouseUp()
    time.sleep(1.1)
    pya.hotkey("ctrl", "c")
    pya.click(x=x_final, y=y_final)
    return pyperclip.paste()


def chatgpt_finalizou_resposta():
    for tentativa in range(8):
        texto = texto_copiado_pyautogui(
            X_INICIO_RECENTES, Y_INICIO_RECENTES, X_FINAL_RECENTES, Y_FINAL_RECENTES
        )
        if resposta_certa in texto:
            return True
        time.sleep(1)
    return False


X_OPCOES_CHAT = 271
Y_OPCOES_CHAT = 241

X_EXCLUIR_CONVERSA = 379
Y_EXCLUIR_CONVERSA = 325

X_CONFIRMAR_EXCLUIR = 1203
Y_CONFIRMAR_EXCLUIR = 620

X_INICIO_RECENTES = 25
X_FINAL_RECENTES = 208
Y_INICIO_RECENTES = 94
Y_FINAL_RECENTES = 208

resposta_certa = "Recentes"

while True:
    pya.click(x=X_OPCOES_CHAT, y=Y_OPCOES_CHAT)
    time.sleep(0.1)
    pya.click(x=X_EXCLUIR_CONVERSA, y=Y_EXCLUIR_CONVERSA)
    time.sleep(0.1)
    pya.click(x=X_CONFIRMAR_EXCLUIR, y=Y_CONFIRMAR_EXCLUIR)
    if chatgpt_finalizou_resposta():
        break
