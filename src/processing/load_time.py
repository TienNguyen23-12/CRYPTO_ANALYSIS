import pandas as pd

def get_time_range(csv_path = 'data/cleaned_coin.csv'):
    df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    return [df.index.min(), df.index.max()]

