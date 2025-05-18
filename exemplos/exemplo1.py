print("Teste dentro do Python")
import requests
print("Importação feita")
resposta = requests.get("https://www.google.pt/")
print(resposta.text)

