import numpy as np
import pandas as pd

def summarize_csv(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.drop_duplicates()
    df = df.dropna(subset=['temp'])
    result = df.groupby('station')['temp'].agg(['mean', 'count'])
    result = result.rename(columns={'mean': 'mean_temp', 'count': 'n'})
    result['mean_temp'] = result['mean_temp'].round(1)
    result = result.sort_index().reset_index()
    result.to_csv(output_path, index=False)
    return len(result)

print(summarize_csv("./someCSV.csv","./summary.csv"))