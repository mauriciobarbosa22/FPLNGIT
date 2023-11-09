'''
Dividir um texto por frases (marcar o fim de frase com um caracter especial '||')
lista de frases ( uma frase em cada linha)


abreviaturas
linha em branco
open ficheiro
'''

import re
abreviaturas = 'D Sr P V S'.split()
#texto2 = '''Esta linda frase. Foi interrompida bruscamente por D. Sesbatiao! Paciência,
#Acham bem??? Fim'''

def fase1(texto):
    fimfrase = r'(\.\.\.|[!?]+|[.]|\n\n+)' #() capturam partes (guarda o grupo que fez matching no meio, e o primeiro grupo é identificado por \1, segundo \2)
    for a in abreviaturas:
        texto = re.sub(rf'{a}\.', rf'{a}\#', texto)
    texto = re.sub(fimfrase, r'\1||\n', texto)  #\1 remete para a captura 1
    for a in abreviaturas:
        texto = re.sub(rf'{a}#', rf'{a}\.', texto)
    return texto

#fase1(texto2)


#f1 = fase1(texto)

def fase2(texto):
    frases = re.split(r'\s*\|\|\s*', texto) #\s todos os espaços 
    return frases

#lf = fase2(f1)

#print(lf)

def fase3(lf):
    numero = 0
    for frase in lf:
        frase = re.sub(r'\n', r' ', frase)
        
        #if not frase.isspace():
        if len(frase) > 0: # ou if frase
            numero += 1
            print(numero, frase)


#fase3(lf)

livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto = open(livro, 'r', encoding='UTF-8').read()

f1 = fase1(texto)
lf = fase2(f1)
f3 = fase3(lf)

