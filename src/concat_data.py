import os
import glob
import pandas as pd

def concat_datasets():
    os.chdir("../data")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    print(f"SHAPE {sum([pd.read_csv(f).shape[0] for f in all_filenames if (f != 'full_data.csv' and f != 'state_source.csv')])}")
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames if (f != 'full_data.csv' and f != 'state_source.csv')])
    
    source_df = pd.read_csv("state_source.csv")
    combined_csv = combined_csv.reset_index()
    combined_csv = combined_csv.drop(columns=["index"])
    links = []

    for index in range(combined_csv.shape[0]):
        state = combined_csv.loc[index, "estado"]
        link_index = source_df["estado"] == state
        link = source_df.loc[link_index,"link"]
        links.append(link.values[0])
    combined_csv["Fonte"] = links
    print(combined_csv)
    combined_csv.to_csv("full_data.csv", index=False)
    
if __name__ == "__main__":
    concat_datasets()
