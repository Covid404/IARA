import pandas as pd


path_file = "data/dados_mg.csv"


def clean_data_mg(path_file: str = path_file) -> pd.DataFrame:
    df = pd.read_csv(path_file)
    df['objeto'] = df['OBJETO_PROCESSO'].str.lower()
    
    index = df['objeto'].str.contains('aquisição de ventiladores')
    
    df = df.loc[index, ["objeto", "QUANTIDADE_HOMOLOGADA", 
                            "VALOR_HOMOLOGADO_UNITARIO",
                          "DATA_PUBLICACAO"]]
    df.columns = ["nome", "quantidade", "preco", "data"]
    df['estado'] = ['MG']*df.shape[0]
    return df



if __name__ == "__main__":
    print(clean_data_mg())
