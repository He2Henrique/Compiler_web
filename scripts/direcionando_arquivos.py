import os


def listar_arquivos(caminho_da_pasta):
    # Lista todos os arquivos na pasta especificada
    arquivos = os.listdir(caminho_da_pasta)
    return arquivos


def listar_arquivos_na_pasta_atual():
    # Obtém o diretório atual do arquivo em execução
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Lista todos os arquivos na pasta atual
    arquivos = os.listdir(diretorio_atual)
    return arquivos

# ler txt


def listar_pastas_acima(alvo, quant):
    # Diretório atual do arquivo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    position = diretorio_atual

    while quant > 0:
        # Voltar uma pasta
        position = os.path.dirname(position)
        

        outro_diretorio = os.path.join(position, alvo)

        # Verificar se o diretório existe
        if os.path.exists(outro_diretorio):
            # Listar os arquivos na outra pasta
            arquivos = os.listdir(outro_diretorio)
            return arquivos, outro_diretorio
        else:
            print(f"O diretório {outro_diretorio} não existe.")
        quant -= 1
    return None


def chose_arq(lis, caminho):
    for i, e in enumerate(lis):
        print(f"{i+1} {e}")
    try:
        decision = int(input("escolha um arquivo: "))
    except ValueError:
        print("erro decisão nao e um numero inteiro")

    decision -= 1
    if decision in range(0, len(lis)):
        return f"{caminho}\{lis[decision]}"
