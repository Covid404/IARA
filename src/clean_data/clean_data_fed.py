import pandas as pd


path_file = "../../raw_data/compras_federais.csv"


def clean_data_fed(path_file: str = path_file) -> pd.DataFrame:
    df = pd.read_csv(path_file)
    df_ventiladores = df[df['ITEM_DESCRICAO'].str.contains('VENTILADOR ART')]
    df_ventiladores = df_ventiladores[~df_ventiladores['ITEM_DESCRICAO'].str.contains('CIRCUITO|MOTOR')]
    df_ventiladores = df_ventiladores[['ITEM_DESCRICAO', 'PRECO_UNITARIO', 'DATA','UF', 'QUANTIDADE']]
    df_ventiladores.columns = ['nome', 'preco', 'data', 'estado', 'quantidade']

    return df_ventiladores



if __name__ == "__main__":
    data = clean_data_fed()
    print(data)
    data.to_csv('../../data/federal.csv', index=False)
