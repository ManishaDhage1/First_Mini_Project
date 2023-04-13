from snowflake.connector.pandas_tools import write_pandas
from snowflake.connector import connect
#import numpy as np
import pandas as pd
def check_blankdata(df):
    for col in df.columns:
        df[col]=df[col].astype(str)
        if(type(df[col].dtype.str.find("object")>=0)):
            df[col] = (df[col]).replace('\W', '', regex=True)
    return df

def SnowConnect():
    conn = connect(
    account='LG97785.us-east-2.aws',
    user = 'AtgeirTeamB',
    password = 'Atgeir@123',
    warehouse = 'WH_01',
    database = 'DEMO_DB',
    schema = 'SCHEMA_01')
    return conn
conn=SnowConnect()
curs=conn.cursor()
df=pd.read_csv("D:/proj_csv/employees.csv")
df1=df.fillna('NULL')
print(df1)
df2=check_blankdata(df1)
print(df2)
r,k=df2.shape
success, num_chunks, num_rows, output = write_pandas(conn=conn,df=df2,table_name='CUSTOMER',database='DEMO_DB',schema='SCHEMA_01',auto_create_table=True, overwrite=True)
table_name='CUSTOMER'
if(success==True):
    if(num_rows==r):
        print("ALL rows {} are inserted in sf table {}".format(num_rows,table_name))
    else:
        print("table is created but rows count doesnt match")
else:
    print("not working")

df=pd.read_csv("D:/proj_csv/customer.csv")

