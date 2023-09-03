import pandas as pd
import openai

#================================== EXPORT =======================================
# Configure sua chave da API OpenAI aqui
openai_api_key = 'SUA-CHAVE'
openai.api_key = openai_api_key

# Leitura do arquivo CSV
df = pd.read_csv('tabela.csv')


#================================== TRANSFORM =======================================
# Função para gerar legendas usando a API OpenAI
def generate_ai_news(tipo_de_empresa, cliente, data_comemorativa):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                "content": "Você é um especialista em marketing digital."},
                {"role": "user", 
                "content": f"Crie uma legenda para um post de Instagram para a empresa de {tipo_de_empresa}, {cliente} sobre a {data_comemorativa} (máximo de 200 caracteres)"}
            ]
        )
        return completion.choices[0].message['content']
    except Exception as e:
        print(f"Erro ao gerar legenda para {cliente}: {str(e)}")
        return None

#================================== LOAD =======================================

# Atualizar a coluna "legenda" com as legendas geradas
for index, row in df.iterrows():
    legenda = generate_ai_news(row['tipo_de_empresa'],row['nome_da_empresa'], row['data_comemorativa'])
    if legenda:
        df.at[index, 'legenda'] = legenda

# Salvar o DataFrame de volta no arquivo CSV
try:
    df.to_csv('tabela_atualizada.csv', index=False)
    # Mensagem de confirmação
    print("Legendas geradas e salvas com sucesso em 'tabela_atualizada.csv'")
except Exception as e:
    print(f"Erro ao salvar o arquivo CSV: {str(e)}")
