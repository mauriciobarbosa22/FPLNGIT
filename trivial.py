import json
import re

def read_questions(nome.py):
    with open(nome, 'w', encoding='utf-8') as f:
        perguntas = json.load(f)
    return perguntas

P = read_questions("trivial.json")s

