from bs4 import BeautifulSoup
import requests

#Extrair os títulos dos artigos de opinião e os respetivos autores

url = "https://www.publico.pt/opiniao"  # Adicione o prefixo https://
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')  # Usar response.content para passar o HTML

# Encontrar todos os elementos h3 com a classe específica (títulos) e os elementos span com a classe do autor
titulos = soup.find_all('h3', class_='card__title headline')
autores = soup.find_all('span', class_='byline__name')

# Extrair os textos dos títulos e dos autores correspondentes
for i in range(len(titulos)):
    titulo = titulos[i].get_text(strip=True)
    autor = autores[i].get_text(strip=True) if i < len(autores) else "Autor não encontrado"
    print(f"{titulo}, {autor}")