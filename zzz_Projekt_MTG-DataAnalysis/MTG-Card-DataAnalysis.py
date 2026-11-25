import pandas as pd
import numpy as np
df = pd.read_json("oracle-cards.jsonl.gz", lines=True, compression="gzip")

# print(df.columns.tolist())
# print(df.info())

print(df["prices"].head(2))


