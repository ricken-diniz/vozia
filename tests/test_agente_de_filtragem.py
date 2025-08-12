from agent.extractor import get_attributes

def test_agent():
    get_attributes('quero ir de natal para sao paulo na proxima sextafeira')
    get_attributes('viagem para daqui a dois dias da paraíba para o pará, uma criança e dois adultos, com limite de 400 reais por passagem')
    get_attributes('Aeroporto Internacional de Natal para aeroporto de guarulhos hoje e a volta daqui a 10 dias')
    get_attributes('viagem do aeroporto de guarulhos com destino em Nova York, desembarque daqui a dois dias de 4pm no fuso local')

if __name__ == '__main__':
    test_agent()
