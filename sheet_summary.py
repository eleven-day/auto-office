import pandas as pd

file = r""

df = pd.read_excel(file,sheet_name=None,header=None,usecols='A:F')

keys = list(df.keys())

df_concat = pd.DataFrame()

for i in keys:
    df1 = df[i]
    df_concat = pd.concat([df_concat, df1])

df_concat.to_excel('./2016明细汇总.xlsx')