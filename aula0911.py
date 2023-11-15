#nome próprio em português (maísculas, com possibilidade de 'de' pelo meio)
#expressao regular que permita descrever um nome próprio, imprimindo para fora o resultado

import re
livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto1 = open(livro, 'r', encoding='utf-8').read()

#texto1 = "O médico João de Deus Martins conseguiu fazer com que a paciente Margarida Carneiro da Silva Lopes e o tivesse alta do hospital Santa Maria no Porto."

def nomesProp(texto):
    pattern = r'\b(?:[A-Z]\w+(?:\s(?:de|da)?\s?[A-Z]\w+)*)(?=\s|\b)'  
    matches = re.findall(pattern, texto)

    return matches

print(nomesProp(texto1))

with open('nomesproprios.txt','w', encoding='UTF=8') as f:
    for nomes in nomesProp(texto1):
        print(nomes, file = f)