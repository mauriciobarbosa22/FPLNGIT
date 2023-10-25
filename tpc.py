# - Calcular capítulos (calcular ocorrencias de # e contar quantos)

livro = 'Camilo-A_Brasileira_de_Prazins.md'
texto = open(livro, 'r', encoding='UTF-8').read()


contador = texto.count('#')

print(f'Número de capítulos: {contador}')

# - Escrever para fora as linhas que contêm o #... (fazer um índice)

def extrair_linhas(texto):
    linhas_capitulo = [line for line in texto.split('\n') if '#' in line]
    return linhas_capitulo

linha = extrair_linhas(texto)

for capitulos in linha:
    print(capitulos)

# - Ocorrências com palavras todas em minusculas

def minusculas(texto):
    palavras = texto.split()
    minusculas = [palavra.lower() for palavra in palavras]
    return len(minusculas)

numero_minusculas = minusculas(texto)
print(f'Número de palavras: {numero_minusculas}')

#- Contagem do número de frases 

import re
def frases(texto):
    n_frases = re.findall(r'[.!?]', texto)
    return len(n_frases)

numero_frases = frases(texto)
print(numero_frases)

# - Qual o comprimento médio da frase em palavras (nº de frases a dividir por nº de palavras)

comp = 59336 / 4102

print(f'Qual é o comprimento médio das frases em palavras?: {comp}')
