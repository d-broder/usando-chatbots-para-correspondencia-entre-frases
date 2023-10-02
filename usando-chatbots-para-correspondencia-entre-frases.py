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
    google_bard_nao_deu_erro()


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
        time.sleep(2)
    # Adicionar comando para apagar conversa
    return False


def google_bard_nao_deu_erro():
    if chatbot_usado == "Google Bard":
        while True:
            conferencia_mensagem_erro = texto_copiado_pyautogui(
                X_INICIO_MENSAGEM_ERRO,
                Y_INICIO_MENSAGEM_ERRO,
                X_FINAL_MENSAGEM_ERRO,
                Y_FINAL_MENSAGEM_ERRO,
            )
            if mensagem_erro not in conferencia_mensagem_erro:
                break
            time.sleep(6)
            pya.click(x=X_CAIXA_TEXTO_CHATGPT, y=Y_CAIXA_TEXTO_CHATGPT)
            time.sleep(0.5)
            pya.hotkey("enter")
            time.sleep(1)


qttd_linhas_a_por_mensagem = 7

# Variáveis para 'qttd_linhas_a_por_mensagem' = 1
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

texto_final_texto = "A sua próxima resposta deverá ser no formato 'Código A, espaço, código B', sendo Código A o código apresentado na primeira linha e 'Código B' a melhor correspondência. Nada mais."

if qttd_linhas_a_por_mensagem > 1:
    texto_bloco_notas = """Chat, é o seguinte. As próximas mensagens eu vou mandar no seguinte formato:

824230 RETIRANDO A VEGETACAO, TRONCOS ATE 5CM DE DIAMETRO E RASPAGEM.
824232 CORTE, RECORTE E REMOCAO DE ARVORES INCL RAIZES DIAM>5<15CM
824236 CORTE, RECORTE E REMOÇÃO DE ÁRVORES INCL.RAIZES 15CM<DIAM<30CM
824239 CORTE, RECORTE E REMOÇÃO DE ÁRVORES INCL.RAIZES 30CM<DIAM<45CM
824241 CORTE, RECORTE E REMOÇÃO DE ÁRVORES INCL.RAIZES 45CM<DIAM<60CM
824242 CORTE, RECORTE E REMOÇÃO DE ÁRVORES INCL.RAIZES 60CM<DIAM<70CM
824243 CORTE, RECORTE E REMOÇÃO DE ÁRVORES INCL.RAIZES 70CM<DIAM<80CM
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
As seis primeiras linhas vou chamar de "Base de Dados A". As demais, vão ser parte do que vou chamar de "Base de Dados B". Para toda mensagem que eu mandar, eu quero que você me forneça, dentro da "Base de Dados B", qual é a melhor correspondência para cada frase da "Base de Dados A". Você vai decidir isso a partir da semântica entre as frases. A resposta você vai me forcecer no seguinte formato:

codigo_a1 codigo_b1
codigo_a2 codigo_b2
codigo_a3 codigo_b3
codigo_a4 codigo_b4
codigo_a5 codigo_b5
codigo_a6 codigo_b6
codigo_a7 codigo_b7

Sendo "código_ax" cada um dos códigos nas cinco primeiras linhas e "código_bx" o código da frase com a melhor correspondência.

Exemplo:

824230 01.01.0001
824232 01.01.0002
824236 01.01.0003
824239 01.01.0004
824241 01.01.0007
824242 01.01.0008
824243 01.01.0009

Além disto, para cada mensagem que eu enviar, você vai adicionar na sua memória interna todas as linhas da "Base de Dados B" para que esta base de dados fique mais completa.

Se, para a frase da "Base de Dados A" não for encontrada nenhuma correspondência, a resposta para este item deverá ser "00.00.0000".

Isto é muito importante: eu quero que a sua mensagem sejam SOMENTE as respostas. Na sua resposta haverá somente algarismos, pontos e espaços, NADA MAIS. A não ser que eu te peça para você voltar a escrever normalmente, eu quero que você se comporte desta forma.

A sua próxima mensagem será você explicando se entendeu ou não. A partir daí, eu vou mandar a mensagem para você associar e você vai seguir o esquema das respostas que expliquei acima. Entendido?"""

    texto_final_texto = """\nA sua próxima resposta deverá ser no formato:
     
codigo_a1 codigo_b1
codigo_a2 codigo_b2
codigo_a3 codigo_b3
codigo_a4 codigo_b4
codigo_a5 codigo_b5
codigo_a6 codigo_b6
codigo_a7 codigo_b7

Sendo "código_ax" cada um dos códigos nas cinco primeiras linhas e "código_bx" o código da frase com a melhor correspondência. Nada mais."""

chatbot_usado = "Google Bard"
# chatbot_usado = "Chat GPT"
linha_a_inicial = 1557
limite_caracteres_por_mensagem = 4096
numero_resultados_por_descricao = 30
linha_a = linha_a_inicial


X_NAVEGADOR = 511
Y_BARRA_DE_TAREFAS = 1063


# Variáveis para o Google Bard:

X_NEW_CHAT = 93
Y_NEW_CHAT = 156

X_CAIXA_TEXTO_CHATGPT = 608
Y_CAIXA_TEXTO_CHATGPT = 945

X_INICIO_REGENERATE = 1383
Y_INICIO_REGENERATE = 300
X_FINAL_REGENERATE = 1700
Y_FINAL_REGENERATE = 400

# Apenas para Chat GPT:
X_DESCER_PAGINA = 1880
Y_DESCER_PAGINA = 900

X_INICIO_RESPOSTA_CHATGPT = 466
Y_INICIO_RESPOSTA_CHATGPT = 309
X_FINAL_RESPOSTA_CHATGPT = 1716
Y_FINAL_RESPOSTA_CHATGPT = 808

resposta_certa = "Acessar outros rascunhos"

X_INICIO_MENSAGEM_ERRO = 40
Y_INICIO_MENSAGEM_ERRO = 972
X_FINAL_MENSAGEM_ERRO = 206
Y_FINAL_MENSAGEM_ERRO = 993

mensagem_erro = "Por enquanto, essa é a resposta que o Bard pode oferecer. Esse recurso é experimental. Tente novamente mais tarde."

if chatbot_usado == "Chat GPT":
    X_NEW_CHAT = 92
    Y_NEW_CHAT = 98

    X_CAIXA_TEXTO_CHATGPT = 750
    Y_CAIXA_TEXTO_CHATGPT = 980

    X_INICIO_REGENERATE = 1340
    X_FINAL_REGENERATE = 1485
    Y_INICIO_REGENERATE = 917
    Y_FINAL_REGENERATE = Y_INICIO_REGENERATE

    resposta_certa = "Regenerate"

    X_INICIO_RESPOSTA_CHATGPT = 672
    X_FINAL_RESPOSTA_CHATGPT = 1567
    Y_INICIO_RESPOSTA_CHATGPT = 140
    Y_FINAL_RESPOSTA_CHATGPT = 825


marcador_tempo = datetime.now().strftime("%Y%m%d%H%M%S")

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

df_resultados = pd.DataFrame()

while linha_a < len(df_a):
    texto_mensagem = ""
    resultados_indice_e_similaridade_total = []
    for linha_a_interna in range(qttd_linhas_a_por_mensagem):
        servico_a = df_a.iloc[linha_a + linha_a_interna]
        codigo_a = servico_a["Código"]
        descricao_a = servico_a["Descrição"]
        texto_mensagem += f"{codigo_a} {descricao_a}\n"

        resultado_indice_e_similaridade = []
        for linha_b, descricao_b in enumerate(lista_descricoes_b):
            similaridade = fuzz.token_sort_ratio(
                descricao_a, descricao_b
            ) + fuzz.token_set_ratio(descricao_a, descricao_b)
            resultado_indice_e_similaridade.append([linha_b, similaridade])
        resultado_indice_e_similaridade.sort(key=lambda x: x[1], reverse=True)
        resultados_indice_e_similaridade_total.append(resultado_indice_e_similaridade)

    codigos_b_resultados_por_linha_a = []
    lista_resultados_codigos_b = []
    cont_numero_linha_b = 0

    while True:
        sair_do_while = False
        for linha_a_interna in range(qttd_linhas_a_por_mensagem):
            if linha_a_interna == qttd_linhas_a_por_mensagem - 1:
                cont_numero_linha_b += 1
            servico_b = df_b.iloc[
                resultados_indice_e_similaridade_total[linha_a_interna][
                    cont_numero_linha_b
                ][0]
            ]
            codigo_b = servico_b["Código"]
            if codigo_b in lista_resultados_codigos_b:
                continue
            descricao_b = servico_b["Descrição"]
            texto_linha_b = f"{codigo_b} {descricao_b}\n"
            numero_caracteres_texto_mensagem = len(
                f"{texto_mensagem}{texto_linha_b}{texto_final_texto}"
            )

            if numero_caracteres_texto_mensagem >= limite_caracteres_por_mensagem:
                sair_do_while = True
                break  # LINHA INDICADA 1

            lista_resultados_codigos_b.append(codigo_b)
            texto_mensagem += texto_linha_b
        if sair_do_while:
            break

    # Adicionar texto no final:
    texto_mensagem += texto_final_texto

    # Obtendo o texto para copiar para o Chat GPT

    erro_resposta = False
    while True:
        if erro_resposta == True or linha_a == linha_a_inicial:
            iniciar_novo_chat()
            if not chatgpt_finalizou_resposta():
                erro_resposta = True
                continue

        # Copiando resultados fuzz para o Chat GPT
        pyperclip.copy(texto_mensagem)
        pya.click(x=X_CAIXA_TEXTO_CHATGPT, y=Y_CAIXA_TEXTO_CHATGPT)
        pya.hotkey("ctrl", "v")
        time.sleep(1)
        pya.hotkey("enter")
        time.sleep(1)
        google_bard_nao_deu_erro()

        # Aguardando resposta do Chat GPT e a copiando
        resultado_codigo_chatgpt = ""
        if not chatgpt_finalizou_resposta():
            erro_resposta = True
            continue

        if chatbot_usado == "Chat GPT" and (
            erro_resposta == True or linha_a == linha_a_inicial
        ):
            pya.click(x=X_DESCER_PAGINA, y=Y_DESCER_PAGINA)
            time.sleep(2)

        resultado_codigo_chatgpt_completo_separado = (
            texto_copiado_pyautogui(
                X_INICIO_RESPOSTA_CHATGPT,
                Y_INICIO_RESPOSTA_CHATGPT,
                X_FINAL_RESPOSTA_CHATGPT,
                Y_FINAL_RESPOSTA_CHATGPT,
            )
            .replace("-", "")
            .replace(",", "")
            .split()
        )

        for linha_a_interna in range(qttd_linhas_a_por_mensagem):
            servico_a = df_a.iloc[linha_a + linha_a_interna]
            codigo_a = str(servico_a["Código"])
            if codigo_a not in resultado_codigo_chatgpt_completo_separado:
                erro_resposta = True
                break
            posicao_a = resultado_codigo_chatgpt_completo_separado.index(codigo_a)
            resposta_codigo_b = resultado_codigo_chatgpt_completo_separado[
                posicao_a + 1
            ]
            if not e_valida(resposta_codigo_b) or len(resposta_codigo_b) not in [
                10,
                11,
            ]:
                if resultado_codigo_chatgpt_completo_separado.count(codigo_a) < 2:
                    erro_resposta = True
                    break
                posicao_a = resultado_codigo_chatgpt_completo_separado.index(
                    codigo_a, posicao_a + 1
                )
                if posicao_a == -1:
                    erro_resposta = True
                    break
                resposta_codigo_b = resultado_codigo_chatgpt_completo_separado[
                    posicao_a + 1
                ]
                if not e_valida(resposta_codigo_b) or len(resposta_codigo_b) not in [
                    10,
                    11,
                ]:
                    erro_resposta = True
                    break
            codigos_b_resultados_por_linha_a.append(resposta_codigo_b)
        else:
            break

    # Adicionando a resposta à data base
    for linha_a_interna in range(qttd_linhas_a_por_mensagem):
        servico_a = df_a.iloc[linha_a + linha_a_interna]
        codigo_a = servico_a["Código"]
        descricao_a = servico_a["Descrição"]
        resultado_lista_codigos.append(
            {
                "Índice": linha_a + linha_a_interna,
                "Código FDE": codigo_a,
                "Código BDCON": codigos_b_resultados_por_linha_a[linha_a_interna],
                "Descrição FDE": descricao_a,
            }
        )
    df_resultados = pd.DataFrame(resultado_lista_codigos)
    try:
        df_resultados.to_csv(caminho_output_csv, index=False)
    except PermissionError:
        pass
    linha_a += qttd_linhas_a_por_mensagem
print("Fim")

try:
    df_resultados.to_excel(caminho_output_xlsx, index=False)
except PermissionError:
    input(
        "A planilha está aberta. Por favor, feche-a e pressione Enter para continuar."
    )
    df_resultados.to_excel(caminho_output_xlsx, index=False)

print("O arquivo foi salvo em: ", caminho_output_xlsx)
