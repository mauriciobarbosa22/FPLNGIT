#nome próprio em português (maísculas, com possibilidade de 'de' pelo meio)
#expressao regular que permita descrever um nome próprio, imprimindo para fora o resultado

import re 
livro = "Camilo-A_Brasileira_de_Prazins.md"
open = open(livro, 'w', encoding='utf=8').read

print(livro)