import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df

#df = pd.read_json('para.json',  orient='records', encoding='utf-8')
with open('scrap/para.json') as f:
    d = json.load(f)
    
    
    
df = json_normalize(d['Registros'])
pa_df = df[df['registro.Descrição do bem ou serviço'].str.contains('Respirador')]#.str.contains("VENTILADOR|CPAP|BIPAP|")]d
pa_df = pa_df[['registro.Descrição do bem ou serviço', 'registro.Data de celebração do contrato', 'registro.Qtde', 'registro.Valor unitário']]
pa_df['estado'] = 'PA'
pa_df.to_csv("pa.csv", index=False)

