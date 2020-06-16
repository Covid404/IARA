import os
import glob
import pandas as pd

def concat_datasets():
    os.chdir("../data")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames if f != 'full_data.csv'])
    combined_csv.to_csv("full_data.csv", index=False)
    
if __name__ == "__main__":
    concat_datasets()