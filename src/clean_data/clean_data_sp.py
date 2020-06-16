import pandas as pd


path_file = "../../raw_data/dados_sp.csv"


def clean_data_sp(path_file: str = path_file) -> pd.DataFrame:
    df = pd.read_csv(path_file, sep=";", encoding = "ISO-8859-1")
    df['objeto'] = df['Item / Finalidade']
    
    ventilador_index = df['objeto'].str.contains("VENTILADOR")
    aquisition_index = df['Descrição Processo'].str.contains("AQUISIÇÃO DE EQUIP")
    index = ventilador_index & aquisition_index
    df = df.loc[index, ["objeto", "Quantidade Item", " Valor Unitário ",
                        "Data Emissão do Pagamento"]]
    print(df)
    df.columns = ["nome", "quantidade", "preco", "data"]
    df['estado'] = ['SP']*df.shape[0]
    return df



if __name__ == "__main__":
    data = clean_data_sp()
    print(data)
    data.to_csv('../../data/dados_sp.csv', index=False)

