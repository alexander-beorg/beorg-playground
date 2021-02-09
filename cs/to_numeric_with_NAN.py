import numpy as np
import pandas as pd

df = pd.DataFrame(
  {
    'name':['1','2','3','4','5'],
    'test':['1','2','abc','4','5']
    })

print(df)
print()
print(pd.to_numeric(df.name, downcast='float'))
print()
t_df_2 = pd.to_numeric(df.test, errors='coerce', downcast='float')
print(t_df_2)
print()
print(t_df_2.astype(pd.Int32Dtype()))
