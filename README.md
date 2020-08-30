# impulso-desafio-estagio
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