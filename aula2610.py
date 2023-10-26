import re
# - Dividir um texto por frases (marcar o fim de frase com um caracter especial '||')
# - lista de frases ( uma frase em cada linha)
# -

#abreviaturas
#linha em branco
#open ficheiro 

texto2 = '''Esta linda frase. Foi interrompida bruscamente por D. Sesbatiao! Paciência,
Acham bem??? Fim'''

def fase1(texto):
    fimfrase = r'(\.\.\.|[!?]+|[.])' #() capturam partes
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
    for frase in lf:
        frase = re.sub(r'\n', r' ', frase)
        numero += 1
        print(numero, frase)

#fase3(lf)

livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto = open(livro, 'r', encoding='UTF-8').read()

f1 = fase1(texto)
lf = fase2(f1)
f3 = fase3(lf)

