import pandas as pd
import numpy as np
df = pd.read_json("./data/raw/oracle-cards.jsonl.gz", lines=True, compression="gzip")

# print(df.columns.tolist())
# print(df.info())

print(df.head(2))


