from pydantic import BaseModel, Field
from typing import Optional

class InformacoesVoo(BaseModel):
    """Estrutura para armazenar informações de uma solicitação de voo."""
    originLocationCode: str = Field(description="O código de 3 digitos do aeroporto de partida do voo seguindo o padrão IATA.")
    destinationLocationCode: str = Field(description="O código de 3 digitos do aeroporto de destino do voo seguindo o padrão IATA.")
    departureDate: str = Field(description="A data de ida da viagem, no formato YYYY-MM-DD.")
    returnDate: Optional[str] = Field(None, description="A data de volta da viagem, se especificada. Formato YYYY-MM-DD.")
    maxPrice: Optional[int] = Field(None, description="O orçamento máximo para a viagem.")
    adults: int = Field(1, description="O número de passageiros para a viagem.")
    currencyCode: str = Field('BRL', description="A moeda utilizada na transação.")
    nonStop: Optional[str] = Field('true', description="Se o voo é sem paradas ('true') ou com escalas ('false').")

class InformacoesHospedagem(BaseModel):
    """Estrutura para armazenar informações de uma solicitação de hospedagem."""
    location: str = Field(description="A localização da hospedagem.")
    checkin: str = Field(description="A data de check-in, no formato YYYY-MM-DD.")
    checkout: Optional[str] = Field(None, description="A data de check-out, no formato YYYY-MM-DD.")
    adults: int = Field(1, description="O número de hóspedes.")
    minPrice: Optional[int] = Field(0, description="O orçamento mínimo para a hospedagem.")
    maxPrice: Optional[int] = Field(None, description="O orçamento máximo para a hospedagem.")