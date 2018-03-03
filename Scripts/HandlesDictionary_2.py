import pandas as pd
import ast


input_file_name=input("Input file name with formart (.csv):")
output_file_name=input("Output file name with csv formart:")

df = pd.read_csv(input_file_name)
#print (df)

df1 = pd.DataFrame(df['bibliographic'].apply(ast.literal_eval).values.tolist())
df1.columns = 'bibliographic.'+ df1.columns

df2 = pd.DataFrame(df['series'].apply(ast.literal_eval).values.tolist())
df2.columns = 'series.'+ df2.columns

col = df.columns.difference(['bibliographic','series'])
df = pd.concat([df[col], df1, df2],axis=1)

df.to_csv(output_file_name, encoding='utf-8', index=False)
