# - Calcular capítulos (calcular ocorrencias de # e contar quantos)
import re 
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
# - Ocorrências com palavras todas em minusculas

palavras = texto.split()    
x = len(palavras)

print(f'Número de palavras: {x}')

#- Contagem do número de frases 


def frases(texto):
    n_frases = re.findall(r'[.!?]', texto)
    return len(n_frases)

numero_frases = frases(texto)
print(numero_frases)

# - Qual o comprimento médio da frase em palavras (nº de frases a dividir por nº de palavras)

comp = 59336 / 4102

print(f'Qual é o comprimento médio das frases em palavras?: {comp}')