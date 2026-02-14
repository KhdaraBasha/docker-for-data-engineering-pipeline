# Import Necessary Modules
import sys
import pandas as pd
import numpy as np


print('arguments ',sys.argv)

month = int(sys.argv[1])

print('input month value ', month)

data = {"day": [1,2], "num_passengers": [3,4]}
df = pd.DataFrame(data)
df['month'] = month
print()
print(df)

df.to_parquet(f"output_{month}.parquet")