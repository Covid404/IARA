import pandas as pd
import numpy as np
from sklearn.covariance import EllipticEnvelope


def run_model(train_data: np.ndarray, predict_data: np.ndarray):
    clf = EllipticEnvelope()
    clf.fit(train_data.reshape(-1, 1))
    outlier = clf.decision_function(predict_data)
    return outlier        


if __name__ == "__main__":

    df = pd.read_csv('../data/full_data.csv')
    array = df[["preco", "quantidade"]].values
    data = []
    indexes = []
    index = 0
    for line in array:
        indexes.append(int(index))
        preco, quantidade = line
        data += [preco]*int(quantidade)
        index += quantidade

    scores = run_model(np.array(data), df['preco'].values.reshape(-1, 1))
    df['anomalo'] = scores
    data.to_csv('../predictions/predictions.csv', index=False)
