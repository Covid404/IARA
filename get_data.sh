#wget https://coronavirus.es.gov.br/Media/Coronavirus/Transparencia/DadosAbertos/dados-contratos-emergenciais-covid-19.csv?v=46 && mv \'dados* raw_data/es.csv

#wget -U "Opera 11.0" https://www.saopaulo.sp.gov.br/wp-content/uploads/2020/06/COVID.csv && mv COVID.csv raw_data/sp.csv


#wget http://www.transparencia.dadosabertos.mg.gov.br/dataset/f70b9258-6a29-47ec-a998-23ac4d74548f/resource/43e125af-3ef0-4afa-87a8-a47b633142f1/download/comprascoronavirus.csv && mv comprascoronavirus.csv raw_data/mg.csv

python scrap/get_pr_data.py

#unzip DISPENSAS_INEXIGIBILIDADE_COVID-2020.zip
#mv TB_DISPENSAS_INEXIGIBILIDADE-2020.csv raw_data/pr.csv
