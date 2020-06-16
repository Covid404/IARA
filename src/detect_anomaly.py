from scipy.stats import zmap
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd


class DetectAnomaly:

    def __init__(self):
        self.num_clusters = 2
        self.kmeans = KMeans(n_clusters=self.num_clusters)

    def fit(self, data: np.ndarray) -> None:
        data = data.reshape(-1, 1)
        self.kmeans.fit(data)
        self.classes = self.kmeans.predict(data)
        print(np.sum(self.classes))
        self.means = []
        self.stddevs = []
        for cluster in range(self.num_clusters):
            index = self.classes == cluster
            mean = np.mean(data[index])
            stddev = np.std(data[index])
            self.means.append(mean)
            self.stddevs.append(stddev)

    def predict(self, value: float) -> bool:
        """Return True if Anomaly and False otherwise"""
        for cluster in range(self.num_clusters):
            if value < self.means[cluster] + 1 * self.stddevs[cluster]:
                return False
        return True
        


if __name__ == "__main__":
    da = DetectAnomaly()
    
    dataset = pd.read_csv('../data/full_data.csv')
    da.fit(dataset['preco'].to_numpy())
    
    for preco in dataset['preco'].to_numpy():
        print(da.predict(preco))

