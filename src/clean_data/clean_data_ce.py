import pandas as pd


path_file = "../../raw_data/ce.csv"


def clean_data_al(path_file: str = path_file) -> pd.DataFrame:    
    
    df = pd.read_csv(path_file, sep=";", encoding = "ISO-8859-1")
    df['objeto'] = df['especificacao'].str.lower()
    
    pulmonar_index = df['objeto'].str.contains('ventilador pulmonar')
    locacao_index = df['objeto'].str.contains('locação')
    circuito_index = df['objeto'].str.contains('circuito')
    mecanico_index = df['objeto'].str.contains('ventilador mecânico')
    index = (pulmonar_index | mecanico_index) & (~ locacao_index.astype(bool)) & (~circuito_index.astype(bool))
    df = df.loc[index, ["objeto", "quantidade", 
                            "valorunitario"]]
    df["data"] = [""]*df.shape[0]
    df.columns = ["nome", "quantidade", "preco", "data"]
    #df["data"] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    #df["preco"] = df['preco'].str.replace('.', "")
    df["preco"] = df['preco'].str.replace(',', ".")
    #df["preco"] = pd.to_numeric(df['preco'])
    df['estado'] = ['CE']*df.shape[0]
    df = df.iloc[:-1]
    return df



if __name__ == "__main__":
    data = clean_data_al()
    data.to_csv("../../data/dados_ce.csv", index=False)
