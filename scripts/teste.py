from script import *
from direcionando_arquivos import listar_pastas_acima


content = ""


arq, pos = listar_pastas_acima("arquivos", 3)


txt = open_txt(f"{pos}\\{arq[0]}")
code = read_json(f"{pos}\\{arq[1]}")

# transforma o bloco de texto em uma sequencia de frases usando ";" como parametro para separação
instru_s = code_words(txt)


# contruindo o interpretador
for instru in instru_s:
    paragafo = process(instru, code)
    content += paragafo + "\n\n"


print(content)
