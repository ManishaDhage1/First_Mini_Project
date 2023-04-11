
import pandas as pd
print("Hello World")
df=pd.read_csv('adult_data.csv', error_bad_lines=False)
print(df)
print(df.tail(10))