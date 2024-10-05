
import json

name = "meu site"
lang = "pt-br"
content = f""
html_content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
</head>
<body>
    {content}

</body>
</html>"""
content = ""


def open_txt(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return text


def rig_json(file_name, data):
    with open(file_name, 'a', encoding='utf-8') as file:
        # Converte o dicionário em JSON e escreve no arquivo
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        # Carrega o conteúdo do arquivo como um objeto Python
        data = json.load(file)
    return data


def right_txt(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        # Escreve o conteúdo no arquivo
        file.write(content)


def clean_string(txt):

    txt = txt.replace("\n", "")  # elimina caracteres de new line
    txt = ' '.join(txt.split())  # elimina espaços em branco desnecessarios
    return txt


def code_words(txt):  # processo de tokenazação.
    # quando utiliza-se split ele vai usar como ponto de referencia o ; para separa o conteudo logo ultimo elemento não é o ; e sim um espaço vasio
    txt = clean_string(txt)
    txt = txt.split(';')
    txt.pop()  # logo é nessecario eliminar o ultimo elemento da lista
    # se usar o f ele ira formata o conteudo
    txt = [f"{linha.strip()}" for linha in txt]

    return txt


def process(instruction, code, tabs=0):
    if ">>" in instruction:
        tabs += 1
        tokens, rest = instruction.split(">>", 1)

        tags = process(rest, code, tabs)

    else:
        tokens = instruction
        tags = ""  # e aqui as tags se ouver uma dentro

    tokens = tokens.split()
    paragrafo = None
    p = None
    for i in tokens:  # utilizado para construir o cabeçalho da tag

        if i in code and paragrafo is None:
            paragrafo = code[i]  # Inicia o parágrafo com o valor de 'code[i]'
            p = i  # Marca o índice atual

        try:
            # Verifica se 'i' está contido dentro do valor de 'code[p]'
            if p and i in code[p]:
                pass  # Apenas um exemplo, aqui vai sua lógica
        except KeyError:  # Usar KeyError, pois é o erro esperado ao acessar um dicionário com chave inválida
            print("Elemento não encontrado")

    configs = ""  # que futuramente ira originar a config
    txt_box = tags   # aqui e o bloco aninhado completo
    if paragrafo:
        paragrafo = paragrafo.format(configs, txt_box)

    else:
        paragrafo = "Elemento não encontrado no código."
    return paragrafo
