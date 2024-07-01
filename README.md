# Tradutor LLM

Este projeto é uma aplicação Streamlit para tradução de textos usando modelos de Tradução Automática da Hugging Face, como MarianMTModel. O objetivo é fornecer uma interface simples para tradução de diferentes línguas.

## Pré-requisitos

Certifique-se de ter Python instalado no seu sistema. Recomenda-se usar um ambiente virtual para manter as dependências do projeto isoladas de outras instalações do Python.

## Configuração do Ambiente

Para configurar o ambiente para este projeto, siga estas etapas:

1. Crie e ative um ambiente virtual:

    ```cmd
    python -m venv .venv
    source .venv/bin/activate  # Para Mac/Linux
    .venv\Scripts\activate     # Para Windows
    ```

2. Instale as dependências do projeto a partir do arquivo requirements.txt:

    ```cmd
    pip install -r requirements.txt
    ```

## Uso

Para executar a aplicação Streamlit, use o comando:

```cmd
streamlit run main.py
```

Isso iniciará a aplicação no navegador padrão, onde você poderá carregar textos para tradução e visualizar os resultados.
