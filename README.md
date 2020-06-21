# IARA

A IARA é a Inteligência Artificial desenvolvida por nós para verifica quão suspeita é uma compra.
Esse repositório é responsável pelas partes de *web scraping*, *data wrangling*
e *machine learning*.

## Como Funciona?

### Web Scraping

Técnica que consiste em extrair os dados de websites automaticamente. No caso do Observatório, os dados são extraídos dos portais de transparência estaduais, então foi necessário criar um programa específico para cada portal. Nessa etapa, utilizamos a ferramenta Selenium.

### Data Wrangling

Com os dados obtidos, agora fazemos a limpeza, selecionamos os dados apenas de ventiladores, obtemos os valores de compras e deixamos em um formato utilizável. Nessa etapa, utilizamos as ferramentas Pandas e Numpy

### Machine Learning

Aqui é onde é a IARA realiza a detecção de anomalias a partir dos dados obtidos. O algoritmo que utilizamos é o Minimum Covariance Determinant Estimator, que detecta outliers (exemplos que fogem do padrão) em conjuntos de dados que estão distribuidos de forma normal. Para isso, utilizamos a biblioteca Scikit-Learn.


## Fonte dos Dados:

* [AL](http://transparencia.al.gov.br/despesa/despesas-com-covid19/)
* [AP](http://www.transparencia.ap.gov.br/consulta/2/496/despesas/)
* [BA](http://www.saude.ba.gov.br/temasdesaude/coronavirus/contratacoes-covid19/)
* [BR](https://www.comprasgovernamentais.gov.br/index.php/transparencia/60-transparencia/1313-transparencia-dos-dados-de-compras-para-o-covid-19)
* [CE](https://cearatransparente.ce.gov.br/portal-da-transparencia/paginas/coronavirus-despesas)
* [ES](https://coronavirus.es.gov.br/contratos-emergenciais)
* [MG](http://www.transparencia.dadosabertos.mg.gov.br/dataset/contratacoes-coronavirus)
* [MS](http://www.comprascoronavirus.ms.gov.br/)
* [MT](http://www.transparencia.mt.gov.br/-/contratos-covid-19)
* [PA](https://transparenciacovid19.pa.gov.br/covid.json)
* [PE](https://comprasemergenciaiscovid19.saude.pe.gov.br/)
* [PI](https://sistemas.tce.pi.gov.br/contratosweb/mural/?s=covid)
* [PR](http://www.transparencia.pr.gov.br/pte/compras/dispensasInexigibilidade?windowId=adf)
* [RJ](http://painel.saude.rj.gov.br/contratos/transparencia.html)
* [RN](http://transparencia.rn.gov.br/covid)
* [RO](http://www.transparencia.ro.gov.br/Grafico/DespesasCOVID19)
* [RR](http://www.transparencia.rr.gov.br/index.php/roraima-contra-o-coronavirus/consulta-despesas-covid19)
* [SP](https://www.saopaulo.sp.gov.br/coronavirus/transparencia/)
