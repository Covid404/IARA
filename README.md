![logo](doc/logo_desc.png)

O Observatório de Compras Emergenciais é um sistema que utiliza inteligência 
artificial para monitorar os 
gastos públicos no combate à COVID-19. Com a pandemia, o poder público realizou
diversas compras sem o devido processo de licitação e isso é sem dúvida
necessário considerando o cenário que estamos. Porém, esse tipo de compra pode
gerar irregularidades como vemos frequentemente na imprensa.

O problema é que todo o trabalho de monitoramento após essas compras tem que ser feito de forma manual.
Com a ciência de dados, o Observatório de Compras Emergenciais é capaz de 
alertar um gasto suspeito, destoante de todos os outros de mesmo tipo feitos 
pelo país. Ele funciona 
consultando e analisando periodicamente os gastos das secretarias estaduais. 
O sistema preza pela visualização simples
e intuitiva dos gastos e tem como seu público alvo os órgãos fiscalizadores, 
ONGs, imprensa e sociedade civil. 

Site: https://covis-dashboard.herokuapp.com/

Repositorio do Site: https://github.com/Covid404/COVIS-dashboard

## Como Funciona?

O Observatório usa diversas técnicas e tecnologias para monitorar as compras
(apenas de ventiladores pulmonares por enquanto) e determinar o nível de anomalia de 
cada compra, o chamado *suspeitômetro*. O sistema determina
o quanto cada compra é suspeita, e não se houve realmente fraude. A tarefa de 
verificação de fraude deve ser feita através de um trabalho investigativo, o 
qual não é o papel do Observatório. O papel do sistema é agilizar o processo
investigativo informando aos agentes fiscalizadores quais compras possuem uma 
maior probabilidade de serem irregulares.

## Como foi Feito?

Toda a solução foi implementada na linguagem de programação *Python*.

### Web Scraping

Técnica que consiste em extrair os dados de websites automaticamente. No caso 
do Observatório, os dados são extraídos dos portais de transparência estaduais, então foi necessário criar um programa específico para cada portal. Nessa etapa, utilizamos a ferramenta *Selenium*.

### Data Wrangling

Com os dados obtidos, agora fazemos a limpeza, selecionamos os dados apenas de ventiladores, obtemos os valores de compras e deixamos em um formato utilizável. Nessa etapa, utilizamos as ferramentas *Pandas* e *Numpy*

### Machine Learning

Aqui é onde é feita a detecção de anomalias a partir dos dados obtidos. O 
algoritmo que utilizamos é o *Minimum Covariance Determinant Estimator*, que 
detecta *outliers* (exemplos que fogem do padrão) em conjuntos de dados que estão distribuidos de forma normal. Para isso, utilizamos a biblioteca *Scikit-Learn*.

### Web Development

Parte em que é feita a apresentação de dados de forma acessível. Os dados são 
apresentados no formato de tabelas e *heatmap*, com cores que indicam 
características dos dados, como quão suspeita é uma compra. Utilizamos aqui o 
*framework* de desenvolvimento web *Dash* e a biblioteca *Plotly* para visualização de dados. 

## Quem Somos?

Somos estudantes da Universidade Federal do Pará - UFPA que desenvolveram esse
sistema durante o Hackaton Serpro 2020. O Hackaton foi criado com o objetivo de
desenvolver soluções para reduzir os impactos causados pela pandemia.

* Líder: Aian Shay
* Web Dev: Alberto Sobrinho
* Web Dev: Pedro Arouck
* Data Analyst: Renan Cunha
* Data Analyst: Renato Mota

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
