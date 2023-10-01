import time
from datetime import datetime

# import Levenshtein
import pandas as pd
import pyautogui as pya
import pyperclip
from thefuzz import fuzz


def e_valida(string):
    for letra in string:
        if not letra.isdigit() and letra != ".":
            return False
    return True


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


def iniciar_novo_chat():
    pya.click(x=X_NEW_CHAT, y=Y_NEW_CHAT)
    time.sleep(1)
    pya.click(x=X_CAIXA_TEXTO_CHATGPT, y=Y_CAIXA_TEXTO_CHATGPT)
    pyperclip.copy(texto_bloco_notas)
    pya.hotkey("ctrl", "v")
    time.sleep(0.5)
    pya.hotkey("enter")
    time.sleep(1)


def chatgpt_finalizou_resposta():
    for tentativa in range(8):
        texto = texto_copiado_pyautogui(
            X_INICIO_REGENERATE,
            Y_INICIO_REGENERATE,
            X_FINAL_REGENERATE,
            Y_INICIO_REGENERATE,
        )
        if resposta_certa in texto:
            return True
        time.sleep(1)
    return False


texto_bloco_notas = """Chat, é o seguinte. As próximas mensagens eu vou mandar no seguinte formato:

824230 RETIRANDO A VEGETACAO, TRONCOS ATE 5CM DE DIAMETRO E RASPAGEM.
01.01.0001 Limpeza manual superficial de terreno - capina
01.01.0002 Corte de capoeira fina c/ foice ou facão
01.01.0003 Limpeza mecanizada de terreno c/ árvores de de Ø até 15 cm c/ trator sobre esteiras
01.01.0004 Raspagem mecanizada do terreno até 40 cm de profundidade c/ trator sobre esteiras
01.01.0007 Limpeza mecanizada do terreno, inclusive troncos com diâmetro acima de 15 cm até 50 cm, com caminhão à disposição dentro da obra, até o raio de 1 km
01.01.0008 Corte e derrubada de eucalipto (1° corte) - idade até 4 anos
01.01.0009 Corte e derrubada de eucalipto (1° corte) - idade acima de 4 anos
01.02.0001 Demolição de alvenaria de tijolo comum, c/ reaproveitamento
01.02.0002 Demolição de alvenaria de ttijolo sem reaproveitamento
01.02.0003 Demolição de assoalho de madeira ou tábua
01.02.0004 Demolição de cobertura de telha cerâmica  - mão de obra
01.02.0005 Demolição de cobertura de telha ondulada de fibrocimento somente mão de obra
01.02.0006 Demolição de concreto c/ ferramentas manuais
01.02.0007 Demolição de edificação de alvenaria
01.02.0008 Demolição de estrutura de madeira de telhado


Todas as linhas vão ser divididas em "código" (no começo) e "frase" (o restante).
A primeira linha vou chamar de "linha de referência". As demais, vão ser parte do que vou chamar de "Base de Dados B". Para toda mensagem que eu mandar, eu quero que você me forneça, dentro da "Base de Dados B", qual é a melhor correspondência para a "linha de referência". Você vai decidir isso a partir da semântica entre as frases. A resposta você vai me forcecer no seguinte formato:

"Código de referência" "Código da melhor correspondência dentro de base de dados B"

(código, espaço e código)

Exemplo:

824230 01.01.0001

Além disto, para cada mensagem que eu enviar, você vai adicionar na sua memória interna todas as linhas da "Base de Dados B" para que esta base de dados fique mais completa.

Isto é muito importante: eu quero que a sua mensagem seja SOMENTE a resposta (código, espaço, código). Na sua resposta haverá somente algarismos, pontos e espaços, NADA MAIS. A não ser que eu te peça para você voltar a escrever normalmente, eu quero que você se comporte desta forma.

A sua próxima mensagem será você explicando se entendeu ou não. A partir daí, eu vou mandar a mensagem para você associar e você vai seguir o esquema das respostas que expliquei acima. Entendido?"""

marcador_tempo = datetime.now().strftime("%Y%m%d%H%M%S")

numero_resultados_por_descricao = 30
linha_a = 24

# Variáveis para o Google Bard
X_NAVEGADOR = 511
Y_BARRA_DE_TAREFAS = 1063

X_NEW_CHAT = 93
Y_NEW_CHAT = 156

X_CAIXA_TEXTO_CHATGPT = 608
Y_CAIXA_TEXTO_CHATGPT = 945

X_INICIO_REGENERATE = 1383
X_FINAL_REGENERATE = 1700
Y_INICIO_REGENERATE = 300
Y_FINAL_REGENERATE = 400
resposta_certa = "Acessar outros rascunhos"

X_INICIO_RESPOSTA_CHATGPT = 466
X_FINAL_RESPOSTA_CHATGPT = 1716
Y_INICIO_RESPOSTA_CHATGPT = 309
Y_FINAL_RESPOSTA_CHATGPT = 808


"""
# Variáveis para o Chat GPT

X_NEW_CHAT = 92
Y_NEW_CHAT = 98

X_CAIXA_TEXTO_CHATGPT = 750
Y_CAIXA_TEXTO_CHATGPT = 980

X_INICIO_REGENERATE = 1340
X_FINAL_REGENERATE = 1485
Y_REGENERATE = 917
resposta_certa = "Regenerate"

X_INICIO_RESPOSTA_CHATGPT = 762
X_FINAL_RESPOSTA_CHATGPT = 1300
Y_RESPOSTA_CHATGPT = 798

X_DESCER_PAGINA = 1880
Y_DESCER_PAGINA = 900
"""

print("Iniciando...")

pya.click(x=X_NAVEGADOR, y=Y_BARRA_DE_TAREFAS)
time.sleep(0.1)

resultado_lista_codigos = []

caminho_input_xlsx = "D:/Users/danie/OneDrive/Área de Trabalho/BID/2023.08.17/Associação BDCON - FDE.xlsx"
df_a = pd.read_excel(caminho_input_xlsx, sheet_name="FDE-Serv")
df_b = pd.read_excel(caminho_input_xlsx, sheet_name="BDCON-Serv")

caminho_output = (
    caminho_input_xlsx.replace(".xlsx", "")
    + " - Resultado Chat GPT - Lista Códigos - "
    + marcador_tempo
)
caminho_output_xlsx = caminho_output + ".xlsx"
caminho_output_csv = caminho_output + " - Temp.csv"

lista_descricoes_a = df_a["Descrição"].tolist()
lista_descricoes_b = df_b["Descrição"].tolist()

while linha_a < len(df_a):
    servico_a = df_a.iloc[linha_a]
    descricao_a = servico_a["Descrição"]
    resultado_indice_e_similaridade = []
    for linha_b, descricao_b in enumerate(lista_descricoes_b):
        similaridade = fuzz.token_sort_ratio(
            descricao_a, descricao_b
        ) + fuzz.token_set_ratio(descricao_a, descricao_b)
        if len(resultado_indice_e_similaridade) < numero_resultados_por_descricao:
            resultado_indice_e_similaridade.append([linha_b, similaridade])
        else:
            resultado_indice_e_similaridade.sort(key=lambda x: x[1], reverse=True)
            if similaridade > resultado_indice_e_similaridade[-1][1]:
                resultado_indice_e_similaridade[-1] = [linha_b, similaridade]
    resultado_indice_e_similaridade.sort(key=lambda x: x[1], reverse=True)

    # Obtendo o texto para copiar para o Chat GPT
    resultados_linha_a = f"{servico_a['Código']} {servico_a['Descrição']}\n"
    for n in range(numero_resultados_por_descricao):
        resultados_linha_a += f"{str(df_b.loc[resultado_indice_e_similaridade[n][0], 'Código'])} {str(df_b.loc[resultado_indice_e_similaridade[n][0],'Descrição'])}\n"
    resultados_linha_a += "\nA sua próxima resposta deverá ser no formato 'Código A, espaço, código B', sendo Código A o código apresentado na primeira linha e 'Código B' a melhor correspondência. Nada mais."

    erro_resposta = False
    while True:
        if erro_resposta == True or linha_a == 0:
            iniciar_novo_chat()
            if not chatgpt_finalizou_resposta():
                erro_resposta = True
                continue

        # Copiando resultados fuzz para o Chat GPT
        pyperclip.copy(resultados_linha_a)
        pya.click(x=X_CAIXA_TEXTO_CHATGPT, y=Y_CAIXA_TEXTO_CHATGPT)
        pya.hotkey("ctrl", "v")
        time.sleep(1)
        pya.hotkey("enter")

        # Aguardando resposta do Chat GPT e a copiando
        resultado_codigo_chatgpt = ""
        if not chatgpt_finalizou_resposta():
            erro_resposta = True
            continue

        # time.sleep(1)
        # if linha_a == 0:
        #     pya.click(x=X_DESCER_PAGINA, y=Y_DESCER_PAGINA)
        #     time.sleep(2)

        resultado_codigo_chatgpt_completo = texto_copiado_pyautogui(
            X_INICIO_RESPOSTA_CHATGPT,
            Y_INICIO_RESPOSTA_CHATGPT,
            X_FINAL_RESPOSTA_CHATGPT,
            Y_FINAL_RESPOSTA_CHATGPT,
        )
        indice_letra_inicial = resultado_codigo_chatgpt_completo.find(
            str(servico_a["Código"])
        )
        if indice_letra_inicial == -1:
            erro_resposta = True
            continue

        resultado_codigo_chatgpt_completo.replace("-", "").replace(",", "")
        resultado_codigo_chatgpt_completo = resultado_codigo_chatgpt_completo[
            indice_letra_inicial:
        ].strip()
        resultado_codigo_chatgpt = resultado_codigo_chatgpt_completo.split()[1]

        if not e_valida(resultado_codigo_chatgpt) or len(
            resultado_codigo_chatgpt
        ) not in [10, 11]:
            erro_resposta = True
            continue
        print("a")
        break

    # Adicionando a resposta à data base
    resultado_lista_codigos.append(
        {
            "Código FDE": servico_a["Código"],
            "Código BDCON": resultado_codigo_chatgpt,
        }
    )
    df_resultados = pd.DataFrame(resultado_lista_codigos)
    try:
        df_resultados.to_csv(caminho_output_csv, index=False)
    except PermissionError:
        pass
    linha_a += 1
print("Fim")

try:
    df_resultados.to_excel(caminho_output_xlsx, index=False)
except PermissionError:
    input(
        "A planilha está aberta. Por favor, feche-a e pressione Enter para continuar."
    )
    df_resultados.to_excel(caminho_output_xlsx, index=False)

print("O arquivo foi salvo em: ", caminho_output_xlsx)
