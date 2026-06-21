import pandas as pd
import numpy as np

def load_mfm_data(path):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m")
    df = df.set_index("Date")
    df.index = df.index + pd.offsets.MonthEnd(0)
    

    return df


