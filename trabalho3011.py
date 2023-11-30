import re
from collections import Counter

texto = open('folha8.OUT.txt', 'r',encoding='utf-8').read()


#Calcular quantas publicações

def publis(texto):
    dates = texto.count('#DATE')
    print(dates)

publis(texto)

#Extrair lista de # e respetivo numero de ocorrências

def cardinal(texto):
    linhas = texto.split('\n')
    oco = {}
    for linha in linhas:
            if linha.startswith('#DATE'):
                if linha in oco:
                    oco[linha] += 1
                else:
                    oco[linha] = 1
    return oco

contagem = cardinal(texto)

with open('lista_de_pubs.txt', 'w', encoding='utf-8') as f:
      for linha, ocorrencias in contagem.items():
            f.write(f'{linha}: {ocorrencias} publicações\n')


#Que gama de datas estão incluídas no ficheiro

#fazer uma expressao regular que me encontre as mais variadas gamas de datas (tenho que especificar todas), posso, ou nao, retirar as linhas do #DATE


def datas(texto):
    paragrafos = texto.split('\n')
    padrao = (r'\b\d{1,2}/\b\d{1,2}/\b\d{2,4}\b|\b\d{1,2}\b\s\bde\b\s\b\w*\b\s\bde\b\sd{2,4}|\b\d{1,2}-\b\d{1,2}-\b\d{2,4}\b|\b\d{1,2}/b/\b\d{1,2}/\b\d{1,2}|\b\d{1,2}\b\s\bde\b\s\w*\s(?:\bde\b\s\d{2,4}\b)?')
    datas_encontradas = re.findall(padrao, texto)
    return datas_encontradas

lista_datas = datas(texto)

with open('gamas_de_datas.txt', 'w', encoding='utf-8') as f:
     for data in lista_datas:
        f.write(f'{data}\n')




#Saber quais são as palavras mais utilizadas, pode permitir saber qual é o tema mais comum (?)