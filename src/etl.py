# =====================
# EXTRACT
# =====================

# Extração de dados de arquivo csv usando Pandas
import pandas as pd

def dados_usuarios():
    users = pd.read_csv('dados/SDW2025.csv').to_dict(orient='records') # Lê o CSV e converte em dicionário
    for user in users:
        user['news'] = [] # Cria nova chave 'news' para cada id do arquivo CSV carregado
    return users

users = dados_usuarios()


# =====================
# TRANSFORM
# =====================

# Criando mensagem personalizada para cada usuário utilizando API do Groq
from groq import Groq
import os
from dotenv import load_dotenv

# Carregar chave API do env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") # Processo necessário para subir aquivo no GitHub com API Key

client = Groq(api_key=GROQ_API_KEY)

def generate_ai_news(user):
    chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "system",
            "content": "Você é um especialista em marketing bancário."
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos, incluindo o nome no início (máximo de 100 caracteres), sempre exiba somente a mensagem final criada",
        }
    ],
     model="groq/compound"
)
    return chat_completion.choices[0].message.content

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "description": news
  })
     

# =====================
# LOAD
# =====================

# Salvando em JSON
import json

with open("dados/SDW2025_com_news.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)
