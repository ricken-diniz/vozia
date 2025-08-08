from langchain.prompts import PromptTemplate

def prompt_template():
    prompt_template = """
    Você é um assistente especializado em extrair informações de voos a partir de um texto. Sua tarefa é analisar cuidadosamente a solicitação do usuário, resolver ambiguidade de locais, interpretar corretamente fusos horários e formatar a resposta em JSON conforme o modelo fornecido.

    Hoje é {data}. Utilize essa informação para inferir datas relativas (como "semana que vem" ou "amanhã").

    ---

    📌 **Instruções de Interpretação:**

    1. **Local de partida e destino**:
    - Sempre retorne **nomes de cidades**.
    - Se o usuário mencionar um **estado**, **região** ou **país**, extraia a **cidade capital** ou a **cidade com o aeroporto mais relevante**.
    - Se mencionar um **aeroporto específico**, extraia a **cidade** correspondente, e salve o nome do aeroporto no campo `aeroporto`.

    2. **Fuso horário e horário do voo**:
    - Se o usuário mencionar horário com fuso (ex: "horário de Brasília", "UTC-3", "horário da Índia"), converta e normalize no formato:
        **`HH:MM UTC±HH:MM`**
        Exemplo: `13:00 UTC+05:30`
    - Se apenas um horário for dado sem fuso, use `UTC-03:00` como padrão (Brasil).

    3. **Orçamento, passageiros, bagagens**:
    - Extraia números sempre que possível. Use o padrão se não for especificado.

    ---

    📦 **Formato de Resposta Esperado (em JSON):**
    {format_instructions}

    ---

    📝 **Texto do Usuário:**
    {solicitacao}

    ---

    ✅ **Sua Resposta JSON:**
    """

    return PromptTemplate(
        input_variables= ["solicitacao","format_instructions","data"],
        template=prompt_template,
    )