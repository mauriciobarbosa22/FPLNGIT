import re
# - Dividir um texto por frases (marcar o fim de frase com um caracter especial '||')
# - lista de frases ( uma frase em cada linha)
# -

#EXERCICIO 1 abreviaturas
#EXERCICIO 2 linha em branco
#EXERCICIO 3 open ficheiro 
#EXERCICIO 4 encontrar todos os numeros

#EXERCICIO 1

texto2 = '''Esta linda frase. Foi interrompida bruscamente por D. Sesbatiao! Paciência,
Acham bem??? Fim'''

def fase1(texto):
    fimfrase = r'(\.\.\.|[!?]+|[.]|D.+|S.+|P.+|S.+|V.+)' #() capturam partes
    novotexto = re.sub(fimfrase, r'\1||\n', texto)  #\1 remete para a captura 1
    return novotexto
    
#fase1(texto2)


#f1 = fase1(texto)

def fase2(texto):
    frases = re.split(r'\s*\|\|\s*', texto) #\s todos os espaços 
    return frases

#lf = fase2(f1)

#print(lf)

def fase3(lf):
    numero = 0
    with open('frases.txt', 'w', encoding='UTF=8') as f:
        for frase in lf:
            frase = re.sub(r'\n', r' ', frase)
            numero += 1
            print(numero, frase, file = f)

#fase3(lf)

livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto = open(livro, 'r', encoding='UTF-8').read()

f1 = fase1(texto)
lf = fase2(f1)
f3 = fase3(lf)

padrao = r'\b\d{4}\b'
anos = re.findall(padrao, texto)

for ano in anos:
    print(ano)



