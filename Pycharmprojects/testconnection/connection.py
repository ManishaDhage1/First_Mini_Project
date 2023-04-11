import pandas as pd
import snowflake.connector
from oscrypto._ffi import engine
from snowflake.connector.pandas_tools import write_pandas
from snowflake.connector.pandas_tools import pd_writer

#conn = snowflake.connector.connect(
 #   user='manisha_usr',
  #  password='Freelancer@123',
   # account='pb40865.ap-south-1',
    #warehouse='MANISHA_WH',
    #atabase='Manisha_DB',
    #schema='Manisha_SCH'
    #enable_connection_diag=True
    #)
conn = snowflake.connector.connect(
    user='dhagemanisha',
    password='Freelancer@123',
    account='ku36826.ap-southeast-1',
    warehouse='COMPUTE_WH',
    database='GARDEN_PLANTS',
    schema='FLOWERS'
    #enable_connection_diag=True
    )
print(conn)
print('Connected')
curs = conn.cursor()
curs.execute("select CURRENT_DATE();")
print(curs.fetchone()[0])
#curs.execute("use database 'Manisha_DB';")
#sql = "Create or replace table garden_plants.flowers.load_csv(O_ORDERKEY  varchar,O_CUSTKEY varchar,O_ORDERSTATUS varchar,O_TOTALPRICE varchar,O_ORDERDATE varchar,O_ORDERPRIORITY varchar,O_CLERK varchar,O_SHIPPRIORITY varchar,O_COMMENT varchar)"
#curs.execute(sql)
sql1 = "use database garden_plants"
curs.execute(sql1)
sql3 = "use schema flowers"
curs.execute(sql3)
#sql4 = "CREATE OR REPLACE STREAM ORDER_STAGE_STREAM ON TABLE GARDEN_PLANTS.FLOWERS.LOAD_CSV APPEND_ONLY=TRUE ;"
#curs.execute(sql4)
original = r"C:\Users\satav\Documents\MRD_19_06_21\MRD_Appraisal\Atgeir_Solutions\Learning\SQL_Snowflake\orders.csv"
delimiter = ","
df = pd.read_csv(original, sep=delimiter)
table_name = 'load_csv'
schema = 'flowers'
database = 'garden_plants'

success, num_chunks, num_rows, output = write_pandas(conn, df, table_name, quote_identifiers=False)
print(success,num_chunks,num_rows,output)



