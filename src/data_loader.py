import pandas as pd
import os

def load_data(file_path):
    """loading data"""
    if not os.path.exists(file_path):
        raise FileNotFoundError("The file does not exist or the path you entered is wrong")
    
    print("Loading data from the file {file_path}...")

    df = pd.read_csv(file_path)
    return df
if __name__ == "__main__":
    dataset_path = "..data\Crop_recommendation.csv"
    try:
        crop_data=load_data(dataset_path)
        print("data loaded succesfully")
        print(crop_data.head())
    except Exception as e:
        print("Error fetching the file {e}")