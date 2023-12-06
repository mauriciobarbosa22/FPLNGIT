

"""TRABALHO
- Calcular quantas publicações
- Extrair lista de #
- ... e respetivo número de ocorrências
- Que gama de datas estão incluídas no ficheiro
- Exercício livre"""


#contents = [ 
		#{ "name":"rui", "profissão": "pedreiro", "idade": 34 },
		#{ "name":"eva", "profissão": "sapateiro", "idade": 24 },
		#{ "name":"ana", "profissão": "pedreiro", "idade": 14 },
		#{ "name":"isa", "profissão": "astronauta", "idade": 44 }
#]

import json, sys, re
with open('ex1.json', encoding='UTF-8') as f:
    contents = json.load(f)


for ele in contents:
#    if ele['profissão'] == 'pedreiro':
    if ele['idade'] > 20:
        print(ele["name"], ele["idade"])
    