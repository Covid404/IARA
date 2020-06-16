import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.ensemble import IsolationForest


def run_model(data):
    isolation_forest = IsolationForest(n_estimators=100)
    isolation_forest.fit(data['preco'].values.reshape(-1, 1))
    xx = np.linspace(data['preco'].min(), data['preco'].max(), len(data)).reshape(-1,1)
    anomaly_score = isolation_forest.decision_function(xx)
    outlier = isolation_forest.predict(xx)
    return outlier        
        
    
if __name__ == "__main__":

    data = pd.read_csv('../data/full_data.csv')
    scores = run_model(data)    
    data['anomalo'] = scores

    data.to_csv('../predictions/predictions.csv', index = False)
    
    

