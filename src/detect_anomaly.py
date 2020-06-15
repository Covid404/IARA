import pandas as pd
from scipy.stats import zmap
import numpy as np


data_path = "data/es.csv"


def detect_outlier(new_value: float, series: np.ndarray):
    z_value = zmap([new_value], series)[0]
    if z_value > 3.5:
        return True
    else:
        return False


