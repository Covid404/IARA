import pandas as pd


path_file = "data/dados_pr.csv"


def clean_data_pr(path_file: str = path_file) -> pd.DataFrame:
    df = pd.read_csv(path_file, sep=";")
    df['objeto'] = df['objeto'].str.lower()
    
    ventilometro_index = df['objeto'].str.contains('ventilômetro')
    ventilador_index = df['objeto'].str.contains('ventilador')
    index = ventilometro_index | ventilador_index
    
    df = df.loc[index, ["objeto", "quantidade", "valorunitario",
                          "datapublicacao"]]
    df.columns = ["nome", "quantidade", "preco", "data"]
    df['estado'] = ['PR']*df.shape[0]
    return df



if __name__ == "__main__":
    print(clean_data_pr())
