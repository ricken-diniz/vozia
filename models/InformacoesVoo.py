from pydantic import BaseModel, Field
from typing import Optional

class InformacoesVoo(BaseModel):
    """Estrutura para armazenar informações de uma solicitação de voo."""
    localdepartida: str = Field(description="CIDADE de partida do voo, se for informado um local ou estado, busque a cidade mais próxima ou capital.")
    localdedestino: str = Field(description="CIDADE de destino do voo, se for informado um local ou estado, busque a cidade mais próxima ou capital.") # Corrigido de 'localdeorigem' para clareza
    dataida: str = Field(description="A data de ida da viagem, no formato DD/MM/AAAA.")
    datavolta: Optional[str] = Field(None, description="A data de volta da viagem, se especificada. Formato DD/MM/AAAA.")
    orcamento: Optional[float] = Field(None, description="O orçamento máximo para a viagem.")
    npassageiros: Optional[int] = Field(1, description="O número de passageiros para a viagem, por padrão o mínimo é um.")
    linhaaerea: Optional[str] = Field(None, description="A companhia aérea de preferência, se mencionada.")
    aeroporto: Optional[str] = Field(None, description="O aeroporto específico de partida ou chegada, se mencionado.")
    quantidadedebagagem: Optional[int] = Field(None, description="A quantidade de bagagens a serem despachadas.")
    horaefusohorario: Optional[str] = Field(None, description="A hora específica do voo e seu fuso horário com base no modelo internacional, exemplo: Horário da Índia (UTC+5:30)")