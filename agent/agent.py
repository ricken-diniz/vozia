from transcritor import transcritor
from models.informacoesvoo import InformacoesVoo
from datetime import date
from agent.promptbuilder import prompt_template
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

def get_attributes(input):
    pydantic_parser = PydanticOutputParser(pydantic_object=InformacoesVoo)
    format_instructions = pydantic_parser.get_format_instructions()
    print(format_instructions)
    # input = transcritor('./audioteste.mp3')
    # input = 'Quero ir de Natal para São Paulo na próxima sexta-feira.'
    data = date.today()
    prompt = prompt_template().format(solicitacao=input, format_instructions=format_instructions, data=data)

    api_key = os.getenv("OPENAI_KEY")
    llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
    chain = llm | pydantic_parser

    try:
        resultado = chain.invoke(prompt)
        print(resultado)
        # Agora você pode acessar os dados facilmente:
        print(f"Partida: {resultado.localdepartida}")
        print(f"Destino: {resultado.localdedestino}")
    except Exception as e:
        print(f"Ocorreu um erro ao processar a solicitação: {e}")

if __name__ == '__main__':
    get_attributes('quero ir de natal para sao paulo na proxima sextafeira')

    