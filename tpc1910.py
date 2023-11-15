# - Calcular capítulos (calcular ocorrencias de # e contar quantos)
import re 
from collections import Counter
livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto = open(livro, 'r', encoding='UTF-8').read()


contador = texto.count('#')

print(f'Número de capítulos: {contador}')

# - Escrever para fora as linhas que contêm o #... (fazer um índice)


def extrair_linhas(texto):
    linhas_capitulo = re.findall(r'#.+', texto) #'.+' o ponto  significa quakquer caracter exceto a quebra de linha; '+' significa 1 ou + ocorrências
    return linhas_capitulo

linha = extrair_linhas(texto)


with open('capitulos.txt','w', encoding='UTF=8') as f:
    for capitulos in linha:
        print(capitulos, file = f)


# agora para um ficheiro em html

def extrair_linhas(texto):
    titulos = re.findall(r'#.+', texto) #'.+' o ponto  significa qualquer caracter exceto a quebra de linha; '+' significa 1 ou + ocorrências
    lista_titulos = '\n'.join(titulos)
    with open('capitulos.html','w', encoding='UTF=8') as f:
        print('<h1> A Brasileira de Prazins </h1>', file = f)
        print('<ol>', file = f)
        for tit in titulos:
            #print('<li>', tit, '</li>', file = f)
            print(f'<li> {tit} </li>', file = f)
        print('</ol>', file = f)

extrair_linhas(texto)
'''
<ol>
<li>titulo</li>
</ol>
'''
# - Ocorrências com palavras todas em minusculas

palavras = texto.split()    
x = len(palavras)

print(f'Número de palavras: {x}')

def oco_minusculas(texto):
    palavras = re.findall(r'\w+', texto)
    minusculas = []
    oco = {}
    for palavra in palavras:
        palavra_minuscula = palavra.lower()
        minusculas.append(palavra_minuscula)
        if palavra in oco:
            oco[palavra_minuscula] += 1
        else:
            oco [palavra_minuscula] = 1
            
            #ocoAlfabeto = sorted(oco.items(), key=lambda item: item[1])
            ocoAlfabeto = sorted(oco.items(), key=lambda item: item[1])
        with open('ocoMinusculas.txt', 'w', encoding='UTF=8') as output_file:
            for palavra, ocorrencias in ocoAlfabeto:
                output_file.write(f'{palavra}:{ocorrencias}\n')
#oco_minusculas(texto)




# - Qual o comprimento médio da frase em palavras (nº de frases a dividir por nº de palavras)


def comprimentoMedio(texto):
    palavras = re.findall (r'\w+', texto)
    pontuacao = re.findall(r'\.\.\.|[!?]+|[\.]', texto)
    contador = Counter(pontuacao)
    total = sum(contador.values())
    if total > 0:
        compMedio = len(palavras) / total
    else:
        compMedio = 0
    print('O comprimento médio das frases em palavras é: ', compMedio)
    print(len(pontuacao))
comprimentoMedio(texto)


