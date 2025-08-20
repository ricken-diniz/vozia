from langchain.prompts import PromptTemplate

def prompt_template_flights():
    prompt_template = """
    Você é um assistente especializado em extrair informações de voos a partir de um texto. Sua tarefa é analisar cuidadosamente a solicitação do usuário, resolver ambiguidade de locais, interpretar corretamente fusos horários e formatar a resposta em JSON conforme o modelo fornecido.

    Hoje é {date}. Utilize essa informação para inferir datas relativas (como "semana que vem" ou "amanhã").

    ---

    📌 **Instruções de Interpretação:**

    1. **Local de partida e destino**:
    - Sempre retorne **códigos dos aeroportos** seguindo o padrão IATA em 3 digitos.
        Exemplo: `NYC`
    - Se o usuário mencionar um **estado**, **região** ou **país**, extraia o **codigo do aeroporto referencia**.

    2. **Moeda**:
    - Identifique a moeda (ex: "dólares", "euros") a partir das informações do texto, como o idioma e localizações, extraia a moeda e normalize no formato:
        **`Código da Moeda`**
        Exemplo: `USD`
    - Se nenhuma moeda for mencionada, use `BRL` como padrão (Real Brasileiro).

    3. **Orçamento, passageiros**:
    - Extraia números inteiros sempre que possível. Se o número de passageiros não for especificado, por padrão é 1.

    4. **Voo direto ou com escalas**:
    - Se o usuário mencionar que deseja um voo direto, defina `semParada` como `'true'`. Caso contrário, defina como `'false'`.
    ---

    📦 **Formato de Resposta Esperado (em JSON):**
    {format_instructions}

    ---

    📝 **Texto do Usuário:**
    {input}

    ---

    ✅ **Sua Resposta JSON:**
    """

    return PromptTemplate(
        input_variables= ["input","format_instructions","date"],
        template=prompt_template,
    )

def prompt_template_accommodation():
    prompt_template = """
    Você é um assistente especializado em extrair informações de hospedagens a partir de um texto. Sua tarefa é analisar cuidadosamente a solicitação do usuário e formatar a resposta em JSON conforme o modelo fornecido.

    Hoje é {date}. Utilize essa informação para inferir datas relativas (como "semana que vem" ou "amanhã").

    ---

    📌 **Instruções de Interpretação:**

    **Data**:
    - Se atente em manter o formato `YYYY-MM-DD` para as datas.


    📦 **Formato de Resposta Esperado (em JSON):**
    {format_instructions}

    ---

    📝 **Texto do Usuário:**
    {input}

    ---

    ✅ **Sua Resposta JSON:**
    """
    
    return PromptTemplate(
        input_variables= ["input","format_instructions","date"],
        template=prompt_template,
    )