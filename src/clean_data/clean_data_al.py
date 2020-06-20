import pandas as pd


path_file = "../../raw_data/al.csv"


def clean_data_al(path_file: str = path_file) -> pd.DataFrame:    
    
    with open(path_file, "r") as f:
        lines = f.readlines()

    lines = lines[7:]
    temp_path_file = "/tmp/temp_al.csv"
    with open(temp_path_file, "w") as f:
        f.writelines(lines)

    df = pd.read_csv(temp_path_file, sep=";")
    df['objeto'] = df['OBJETO'].str.lower()
    
    index = df['objeto'].str.contains('ventilador')
    df = df.loc[index, ["objeto", "QUANTIDADE", 
                            "VALOR_UNITARIO",
                          "DATA_CELEBRACAO", 'PROCESSO']]
    df.columns = ["nome", "quantidade", "preco", "data", 'id']
    df["data"] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df["preco"] = df['preco'].str.replace('.', "")
    df["preco"] = df['preco'].str.replace(',', ".")
    df["preco"] = pd.to_numeric(df['preco'])
    df['estado'] = ['AL']*df.shape[0]
    return df



if __name__ == "__main__":
    data = clean_data_al()
    data.to_csv("../../data/dados_al.csv", index=False)
