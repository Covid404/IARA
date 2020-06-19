# Como Funciona?

O COVIS usa diversas técnicas e tecnologias para monitorar as compras de 
ventiladores e determinar o nível de anomalia de cada compra. É bom deixar claro
que o COVIS determina o quanto cada compra é suspeita, e não se houve realmente
fraude. A tarefa de verificação de fraude deve ser feita através de um trabalho
investigativo, possivelmente por órgãos fiscalizadores e imprensa. 

As técnicas utilizadas para o desenvolvimento do sistema são:
*web scraping*, *data wrangling*, *machine learning* e *web development*.
Essas técnicas foram transformadas em módulos, que são executados em sequência
de acorco com a figura abaixo. Toda a solução foi implementada na linguagem de programação
*Python*.

## *Web Scraping*

Técnica que consiste em extrair os dados de *websites* de forma automática. 
No caso do COVIS, os dados são extraídos dos portais de transparência de cada
estado, então foi necessário criar um programa específico para cada portal. 
Nessa etapa, utilizamos a ferramenta *Selenium*.

## *Data Wrangling*

Com os dados obtidos, agora fazemos a limpeza, selecionamos os dados apenas de
ventiladores, obtemos os valores de compras e deixamos em um formato utilizável.
Nessa etapa, utilizamos as ferramentas *Pandas* e *Numpy*.

## *Machine Learning*

Aqui é onde é feita a detecção de anomalias a partir dos dados obtidos.
O algoritmo que utilizamos é o *Minimum Covariance
Determinant Estimator*, que detecta *outliers* (exemplos que fogem do padrão) 
em conjuntos de dados que estão distribuidos de forma normal. Para isso, 
utilizamos a biblioteca *Scikit-Learn*

## *Web Development*

Parte em que é feita a apresentação de dados de forma acessível. Os dados são
apresentados no formato de tabelas e *heatmap*, com cores que indicam
características dos dados, como quão suspeita é uma compra. Utilizamos aqui
o *framework* de desenvolvimento *Django* e a biblioteca *Plotly* para
visualização de dados.
