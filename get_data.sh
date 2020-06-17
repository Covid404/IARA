wget https://coronavirus.es.gov.br/Media/Coronavirus/Transparencia/DadosAbertos/dados-contratos-emergenciais-covid-19.csv?v=46 && mv dados-con* raw_data/es.csv

wget -U "Opera 11.0" https://www.saopaulo.sp.gov.br/wp-content/uploads/2020/06/COVID.csv && mv COVID.csv raw_data/sp.csv


wget http://www.transparencia.dadosabertos.mg.gov.br/dataset/f70b9258-6a29-47ec-a998-23ac4d74548f/resource/43e125af-3ef0-4afa-87a8-a47b633142f1/download/comprascoronavirus.csv && mv comprascoronavirus.csv raw_data/mg.csv

python scrap/get_pr_data.py

unzip scrap/DISPENSAS_INEXIGIBILIDADE_COVID-2020.zip
mv TB_DISPENSAS_INEXIGIBILIDADE-2020.csv raw_data/pr.csv


python scrap/get_al_data.py
mv scrap/Despesas raw_data/al.csv

curl https://transparenciacovid19.pa.gov.br/covid.json > scrap/para.json
python scrap/get_pa_data.py
mv pa.csv raw_data/pa.csv


#wget https://www.compras.rj.gov.br/arquivos/COMPRAS_DIRETAS.zip
wget --no-check-certificate -U "Opera 11.0" https://www.compras.rj.gov.br/arquivos/COMPRAS_DIRETAS.zip
unzip COMPRAS_DIRETAS.zip
mv COMPRAS_DIRETAS.CSV raw_data/rj_diretas.csv

rm -rf *.csv
rm -rf *.zip
rm -rf scrap/*.csv
rm -rf scrap/*.zip
rm -rf scrap/*.json
