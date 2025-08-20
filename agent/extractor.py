from models.informacoes import InformacoesVoo, InformacoesHospedagem
from datetime import date
from models.promptbuilder import prompt_template_flights, prompt_template_accommodation
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def get_attributes(data: str):
    '''
        Extrai informações de voo a partir de uma solicitação em linguagem natural.
            {data}: A solicitação em linguagem natural.
    '''
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_KEY"))

    pydantic_parser_accommodation = PydanticOutputParser(pydantic_object=InformacoesHospedagem)
    format_instructions_accommodation = pydantic_parser_accommodation.get_format_instructions()
    prompt_accommodation = prompt_template_accommodation().format(input=data, format_instructions=format_instructions_accommodation, date=date.today())

    pydantic_parser_flights = PydanticOutputParser(pydantic_object=InformacoesVoo)
    format_instructions_flights = pydantic_parser_flights.get_format_instructions()
    prompt_flights = prompt_template_flights().format(input=data, format_instructions=format_instructions_flights, date=date.today())

    chain_flights = llm | pydantic_parser_flights
    chain_accommodation = llm | pydantic_parser_accommodation

    try:
        dados_extraidos = {}

        resultados_flights = chain_flights.invoke(prompt_flights)
        resultados_accommodation = chain_accommodation.invoke(prompt_accommodation)
        
        dados_extraidos['flight'] = resultados_flights.model_dump()
        dados_extraidos['host'] = resultados_accommodation.model_dump()

        return dados_extraidos
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao processar a solicitação: {e}")


    