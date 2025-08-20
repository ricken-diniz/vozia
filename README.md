# VOZIA
<img width="2563" height="1211" alt="Gemini_Generated_Image_r1g3shr1g3shr1g3" src="https://github.com/user-attachments/assets/1d7c1ba6-f975-46d3-b53e-f4332285d9e0" />
Pesquisa de hospedagens e passagens aéreas a partir do comando de voz utilizando Inteligência Artificial.

Ferramentas utilizadas:
- Whisper
- LangChain, LangGraph
- Pydant, PromptTemplate
- AmadeusAPI
- Airbnb MCP Server
- Estruturação de arquivos python em módulos
- Requests

Para rodar o projeto:

- 1. Instale o ambiente NodeJS para rodar o cliente MCP do Airbnb
```
sudo apt install nodejs npm
```

- 2. Instale as dependências em seu ambiente virtual
```
npm install '@openbnb/mcp-server-airbnb'
pip install -r requirements.txt
```

- 3. Rode o projeto
```
python3 -m agent.graph
```

Se preferir, acesse o tutorial com *Jupyter Notebook* no [Google Colab](https://colab.research.google.com/drive/1AQs6YcckZ6arwl0TmTIxTVTnnOd2GPHC?usp=sharing)