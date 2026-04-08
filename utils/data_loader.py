
import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    file_name = input("Enter dataset file name (inside data folder): ")
    file_path = os.path.join(base_dir, "data", file_name)
    
    df = pd.read_csv(file_path)
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower()
    
    print("\n📊 Available columns:")
    print(list(df.columns))
    
    return df