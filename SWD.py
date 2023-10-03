import openai
# Lembrando, para usar o openai, você tem que ir no prompet de comando do (vs code, no meu caso e usar o comando "pip install openai".
openai_api_key = "sua-chave-da-api-openai"

# Defina a lista de usuários com a estrutura de dados desejada
users = [
    {"name": "User1"},
    {"name": "User2"},
    {"name": "User3"},
]

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
