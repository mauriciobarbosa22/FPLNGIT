import re

texto = open('folha8.OUT.txt', 'r',encoding='utf-8').read()


#Calcular quantas publicações

def publis(texto):
    dates = texto.count('#DATE')
    print(dates)

publis(texto)

#extrair lista de # e respetivo numero de ocorrências

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
            f.write(f'{linha}: {ocorrencias}\n')