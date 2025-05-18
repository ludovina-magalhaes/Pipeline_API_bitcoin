print("Teste dentro do Python")
import requests
print("Importação feita")

# Corrigindo a passagem de parâmetros
response = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 1})
print("Requisição realizada!")

comentarios = response.json()
print(f" total de {len(comentarios)} comentarios encontrados")
print (f"Erro. {response.status_code}- {response.text}") 

