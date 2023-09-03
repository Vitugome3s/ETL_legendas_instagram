# Projeto de Geração de Legendas de Instagram com IA

Este é um projeto que utiliza a tecnologia de IA (Inteligência Artificial) para gerar legendas criativas e relevantes para postagens no Instagram com base em eventos comemorativos de empresas. A IA é alimentada pelo GPT-3.5 Turbo da OpenAI, um dos modelos de linguagem mais avançados disponíveis.

## Como Funciona

1. **Preparação dos Dados**: O projeto começa lendo um arquivo CSV que contém informações sobre empresas e os eventos comemorativos relacionados a elas. Os dados incluem o nome da empresa e a data do evento.

2. **Geração de Legendas**: Para cada empresa e evento comemorativo, o projeto utiliza a API da OpenAI para solicitar à IA a criação de uma legenda para uma postagem no Instagram relacionada ao evento.

3. **Atualização do CSV**: Após gerar a legenda, o projeto atualiza a coluna "legenda" no arquivo CSV original com as legendas geradas.

4. **Salvando Resultados**: Os resultados finais, incluindo as legendas atualizadas, são salvos em um novo arquivo CSV chamado 'tabela_atualizada.csv'.

## Requisitos

- Python 3.x
- Pandas
- OpenAI Python SDK

## Configuração

Antes de executar o projeto, certifique-se de configurar sua chave da API OpenAI no arquivo de código-fonte para habilitar a geração de legendas.

```python
openai_api_key = 'SUA_CHAVE_DA_API_OPENAI'
```

## Como Usar

1. Clone este repositório em seu ambiente local.

2. Instale as dependências necessárias:

```python
pip install pandas openai
```
3. Execute o projeto:

```python
python nome_do_arquivo.py
```
4. Verifique o arquivo 'tabela_atualizada.csv' para ver as legendas geradas atualizadas para cada empresa.
