'''opção m para imprimir apenas as most common 20 (as 20 palavras que mais ocorreram (counter.mostcommon))
criar um regex que funcione como lista negra (se a minha entidade fizesse matching ocm essa regex, deitava fora das entidades ( por exemplo, se tem um dígito, deito fora; se tem um stopword deito fora; etc))
estudar o módulo json'''

import re
from collections import Counter
livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto1 = open(livro, 'r', encoding='utf-8').read()

#texto1 = "O médico João de Deus Martins conseguiu fazer com que a paciente Margarida Carneiro da Silva Lopes tivesse alta do hospital Santa Maria no Porto."

def nomesProp(texto):
    pattern = r'\b([A-ZÁÉÍÓÚÊÔ]\w+(?:\s(?:de|da|do)?\s?[A-Z]\w+)*)(?=\s|\b)'  #\b word boundary   #() captura   # ? é opcional (1 ou nenhum)    \s espaço
    matches = re.findall(pattern, texto)
    return matches

#print(nomesProp(texto1))

with open('nomesproprios.txt','w', encoding='UTF=8') as f:
    for nomes in nomesProp(texto1):
        print(nomes, file = f)


'''opção m para imprimir apenas as most common 20 (as 20 palavras que mais ocorreram (counter.mostcommon))
criar um regex que funcione como lista negra (se a minha entidade fizesse matching ocm essa regex, deitava fora das entidades ( por exemplo, se tem um dígito, deito fora; se tem um stopword deito fora; etc))
estudar o módulo json'''


# Read names from nomesproprios.txt with UTF-8 encoding
with open('nomesproprios.txt', 'r', encoding='utf-8') as names_file:
    names = [name.strip() for name in names_file.readlines()]

# Count occurrences of each name using Counter
name_counts = Counter(names)

# Get the 20 most common names
most_common_names = name_counts.most_common(20)

# Print the 20 most common names
print(most_common_names)