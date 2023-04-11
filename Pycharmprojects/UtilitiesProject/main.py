import pandas as pd
import easylevelutilities

original = r"C:\Users\satav\Documents\MRD_19_06_21\MRD_Appraisal\Atgeir_Solutions\Learning\SQL_Snowflake\orders.csv"
delimiter = ","
df = pd.read_csv(original, sep=delimiter)
print(df)

easylevelutilities .my_function()