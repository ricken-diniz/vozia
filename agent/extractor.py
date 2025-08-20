from models.informacoes import InformacoesVoo
from datetime import date
from agent.promptbuilder import prompt_template_voo, prompt_template_hospedagem
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
import json
import os
from dotenv import load_dotenv
load_dotenv()

def get_attributes(data: str):
    '''
        Extrai informações de voo a partir de uma solicitação em linguagem natural.
            {data}: A solicitação em linguagem natural.
    '''

    pydantic_parser = PydanticOutputParser(pydantic_object=InformacoesVoo)
    format_instructions = pydantic_parser.get_format_instructions()
    prompt_voo = prompt_template_voo().format(input=data, format_instructions=format_instructions, date=date.today())
    prompt_hospedagem = prompt_template_hospedagem().format(input=data, format_instructions=format_instructions, date=date.today())
    
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_KEY"))
    chain = llm | pydantic_parser
    
    try:
        dados_extraidos = {}
        resultados_voo = chain.invoke(prompt_voo)
        resultados_hospedagem = chain.invoke(prompt_hospedagem)
        dados_extraidos['flight'] = resultados_voo.model_dump()
        dados_extraidos['host'] = resultados_hospedagem.model_dump()
    
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao processar a solicitação: {e}")


    