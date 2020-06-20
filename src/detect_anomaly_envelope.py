import pandas as pd
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.preprocessing import MinMaxScaler
from math import log


def run_model(train_data: np.ndarray, predict_data: np.ndarray):
    clf = EllipticEnvelope()
    clf.fit(train_data.reshape(-1, 1))
    outlier = clf.decision_function(predict_data.reshape(-1, 1))
    return outlier        



def make_predictions():
    df = pd.read_csv('data/full_data.csv')
    #df["preco"] = df["preco"].str.replace(".", "")
    #dVf["preco"] = df["precoa"].str.replace(",", ".")
    df["preco"] = pd.to_numeric(df["preco"])
    array = df[["preco", "quantidade"]].values
    data = []
    indexes = []
    index = 0
    for line in array:
        indexes.append(int(index))
        preco, quantidade = line
        data += [preco]*int(quantidade)
        index += quantidade

    scores = run_model(np.array(data), df['preco'].values)
    #scores = 2**scores
    #scores = scores.reshape(-1, 1)
    #scaler = MinMaxScaler(feature_range=(0, 10))
    #scores = scaler.fit_transform(scores)

    #sorted_scores = np.sort(scores)
    #for index in range(-1, len(scores)-1, -1):
    #    score_value = scores[index]
    #    lesser_index = scores[:index-1] < score_value + [False]*abs(index)
    #    scores[lesser_index] = score_value
    
    df['anomalo'] = scores

    df = df.sort_values(by=["preco"], ascending=False)
    df = df.reset_index()
    df = df.drop(columns=["index"])

    
    for index in range(df.shape[0]):
        score_value = df.loc[index, "anomalo"]
        lesser_index = (df.loc[index+1:, 
                               "anomalo"] < score_value).values.tolist()
        lesser_index = [False] * (index + 1) + lesser_index
        df.loc[lesser_index, "anomalo"] = score_value
    
    scaler = MinMaxScaler(feature_range=(0, 10))
    scores = df['anomalo'].values.reshape(-1, 1)
    scores = -1*scores

    df['anomalo'] = scaler.fit_transform(scores)
    df['anomalo'] = df['anomalo'] ** (1/3)
    df['anomalo'] = scaler.fit_transform(df['anomalo'].values.reshape(-1, 1))


    #### add anomalo label
    def set_label(value: float) -> str:
        if value < 10/3:
            return "baixo"
        elif value < 20/3:
            return "medio"
        else:
            return "alto"

    values = [set_label(x) for x in df['anomalo'].values]
    df['anomalo_label'] = values

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df[['preco', 'anomalo', 'anomalo_label']])
    df['data'] = pd.to_datetime(df['data']).dt.strftime('%Y-%m-%d')    
    df['data'] = pd.to_datetime(df['data']).dt.strftime('%d/%m/%Y')
    df['valor_total'] = df['quantidade'].astype(int)*df['preco']
    df.to_csv('predictions/predictions.csv', index=False)
