# impulso-desafio-estagio
## 1. Como comparar municípios? (descritiva)
### Desafio:
Imagine que um gestor público entra hoje no Farol e quer ter a possibilidade de comparar seu município com outros municípios de seu interesse. Com base no que implementamos até hoje no código do Farol, o que você faria para adicionar essa comparação na ferramenta? Nos descreva o passo a passo e a lógica por trás do código: Como apresentaria essa informação? Quais elementos e funções que já temos hoje você usaria? Quais novas funções você criaria?

### Solução:
**Alto Nível:**

Na aba de Farol Covid, depois de ver todos os dados sobre o município selecionado existe a sessão 'COMO SEGUIR COM SEGURANÇA?' com os banners 'SIMULA COVID' e 'SAÚDE EM ORDEM' a ideia seria colocar um terceiro banner com o nome 'COMPARE SEU MUNICÍPIO'.

![banners](como-seguir-com-seguranca.png)

Ao clicar para comparar o município apareceria para o usuário duas barras de seleção iguais a do início do farol covid, com a primeira com o título: "Seu Município" e selecionado os mesmos campos já previamente selecionados pelo usuário no farol, mas com a opção de mudar a seleção. A segunda teria o título 'Município a comparar' e a barra estaria em branco.

![seu municipio](seu-município.png)
![municipio a comparar](município-a-comparar.png)

A ideia é gerar um segundo farol com os dados do segundo município e comparar os índices com os índices do primeiro município. Primeiro apareceriam os dados dos dois municípios, e então uma terceira sessão com as informações de comparação. Por exemplo a caixa 'Ritmo de Contágio' teria uma comparação de em média no município X cada contaminado infecta Z menos pessoas que no município Y. Isso para cada uma das caixas com os dados, sempre utilizando o município do usuário como comparação. Dessa forma o usuário tem ideia dos dados brutos de cada município mas também do tamanho da diferença entre os dois.

**Implementação:**

Primeira parte, no arquivo `src/pages/main.py`, incluir um botão de seleção para a comparação entre as cidades:

```python
import pages.compara_municipios as cm
"""
...

"""
# SELECTION BUTTONS
if session_state.continuation_selection is None:
    session_state.continuation_selection = [False, False]
simula_button_name = "Clique Aqui"  # Simula covid 0space
saude_button_name = "Clique Aqui "  # Saude em ordem 1space
compara_button_name = "Clique Aqui"
if st.button(simula_button_name):
    session_state.continuation_selection = [True, False]
if st.button(saude_button_name):
    session_state.continuation_selection = [False, True]
if st.button(compara_button_name):
    session_state.continuation_selection = [False, True]

utils.stylizeButton(
    simula_button_name,
    """border: 1px solid black;""",
    session_state,
    others={"ui_binSelect": 1},
)

utils.stylizeButton(
    saude_button_name,
    """border: 1px solid black;""",
    session_state,
    others={"ui_binSelect": 2},
)

utils.stylizeButton(
    compara_button_name,
    """border: 1px solid black;""",
    session_state,
    others={"ui_binSelect": 3},

)
"""
...

"""
if session_state.continuation_selection[2]:
        user_analytics.safe_log_event(
            "picked compara_municipios",
            session_state,
            event_args={
                "state": session_state.state_name,
                "health_region": session_state.health_region_name,
                "city": session_state.city_name,
            },
            alternatives=["picked saude_em_ordem", "picked simulacovid","picked compara_municipios"],
        )
        
        cm.main(user_input, indicators, data, config, session_state)
```

O arquivo `src/pages/compara_municipo.py` seria criado e sua função main utilizaria de funções do arquivo `src/pages/main.py`.
Por exemplo para mostrar os indicadores de cada um dos municípios, utilizaria da função `update_indicators()`, para carregar os indicadores dos dois municípios.

Uma nova funcionalidade a ser adicionada ao código é mais cartões na classe `IndicatorsCards`, para poder englobar os cartões de comparação.

```python
IndicatorCards: Dict[str, Indicator] = {
    """
    ...

    """
    IndicatorType.RT_COMPARISON.value: Indicator(
        header="Ritmo de Contágio",
        caption="Cada contaminado infecta em média outras",
        unit="pessoas de diferença",
        left_label="Seu município:",
        right_label="Município comparado:",
    ),
    IndicatorType.SUBNOTIFICATION_RATE.value: Indicator(
        header="Subnotificação",
        caption="A cada 10 pessoas doentes,",
        unit="são diagnosticadas de diferença",
        left_label="Seu município:",
        right_label="Município comparado:",
    ),
    IndicatorType.HOSPITAL_CAPACITY.value: Indicator(
        header="Capacidade Hospitalar",
        caption="Os seus leitos estarão todos ocupados em",
        unit="mês(es) de diferença",
        left_label="Seu município:",
        right_label="Município comparado:",
    ),
    IndicatorType.SOCIAL_ISOLATION.value: Indicator(
        header="Isolamento Social",
        caption="Na última semana, ficaram em casa cerca de",
        unit="das pessoas de diferença",
        left_label="Seu município:",
        right_label="Município comparado:",
    ),
}
```

Para implementar como mostrar as informações comparadas na tela teria que criar uma nova função, no arquivo `src/pages/compara_municipo.py`, que seria parecida com a `update_indicators()` mas para esses novos indicadores de comparação. Que vai simplesmente fazer a diferença dos indicadores de cada município já previamente calculado. Para renderizar na página os cartões, usaria a função `genKPISection` do arquivo `src/pages/utils.py`

## 2. Que tal coletar dados de testagem da Covid-19?
### Desafio:
O Ministério da Saúde disponibiliza hoje em sua Plataforma Integrada de Vigilância em Saúde os dados de testagem dos estados brasileiros. O nível de testagem de um estado é uma variável improtante para determinar o quanto de controle ele tem sobre como a doença está disseminada em sua população. Esta plataforma contém os dados sobre testes RT-PCR realizados em todos os estados até hoje. Você deve criar um script que realiza a raspagem dos dados de exames por estado.

* Implemente este desafio num script chamado app.py em seu repositório privado.
* Seu script app.py deve ter uma função principal que recebe a URL e retornar uma série com o percentual de resultados Posivito/Detectável por estados. Esta função deve já ser chamada no próprio script para testarmos.
* Para avaliação final iremos rodar seu código em https://repl.it/, sugerimos que teste previamente a plataforma.
* O código deve rodar em Python 3.8.2.

### Solução:
A solução foi construída em camadas, cada uma com uma função específica e a camada superior é chamada pelo arquivo `app.py`

**scraping**

*Bibliotecas utilizadas:*

*Selenium*

*BeautifulSoup*

Primeiramente o `beautiful_soup_service.py` faz a raspagem do código fonte da página http://plataforma.saude.gov.br/coronavirus/virus-respiratorios/ para encontrar a url do dashboard feito no kibana que exibe os dados sobre os exames para vírus respiratórios.
Depois o `selenium_service.py` utiliza um objeto da classe `Browser` (classe que extende a classe `selenium.webdriver.Chrome`) para abrir e navegar pelo dashboard, após interagir com a página e abrir a aba que exibe os dados necessários para a análise, a funcão `crawl_kibana_dashboard()` retorna a html completa do que está sendo exibido na tela. Usa-se novamente o `beautiful_soup_service.py`, desta vez para extrair o json que contém as respostas e transformá-lo em dicionário. As manipulações desses objetos são todas orquestradas pelo `scraping_service.py`, sua função principal `scrape_content()` retorna justamente o dicionário com as informações de exames por estado.

**data_treatment**

*Biblioteca utilizada:*

*pandas*

A classe `DataExtraction` contém funções para extrair apenas os dados necessários do dicionário com os dados dos estados, após fazer isso seu método `extract_exams_per_state()` retorna um DataFrame da biblioteca pandas, com as informações extraídas.
O arquivo `analysis_service.py` tem a função de criar uma coluna que calcula, para cada estado, a porcentagem de exames positivos / detectáveis sobre o total de exames daquele estado. A classe `DataTreatmentService` orquestra essas manipulações de dados e sua função `get_positive_percentage_per_state_dataframe` retorna um dataframe apenas com as colunas 'UF' e '% Positivo / Detectável'.

**controller**

Camada mais abstrata, a classe ExamsController chama a camada de scraping, usa seu retorno para chamar a camada de data_treatment e retorna o dataframe obtido para quem chamar seu método `get_positive_percentage_per_state()`.

**app.py**

Possui uma função `main()` que recebe uma url e chama a função `get_positive_percentage_per_state()` mandando essa url como parâmetro e imprime o dataframe obtido na tela.