import snowflake.connector
import os
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

conn = snowflake.connector.connect(
    account = 'ra08800.eu-west-1',
    user = 'dziubaska',
    password = os.environ.get('SNOWSQL_PWD')
)
cur = conn.cursor()
cur.execute("SELECT * from test.public.employees")

# print(cur.fetchall())

# for row in cur:
#     print(row)

df = cur.fetch_pandas_all()
print(df)
