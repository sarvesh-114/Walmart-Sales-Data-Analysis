import pandas as pd
data = pd.read_csv(r'C:\Users\sarvesh jathar\Desktop\Project-Walmart\Walmart.csv', encoding_errors='ignore')
Pdata.head()

data.shape

data.info()

data.describe()

data.isnull().sum()

data.dtypes

data.duplicated().sum()

data.drop_duplicates(inplace=True)

data.shape

data.dropna(inplace = True)

data.isnull().sum()

data.shape

data['unit_price'] = data['unit_price'].str.replace("$", "")

data.head()

data.info()

data['unit_price'].astype('float')

data.head()

data.columns

data['unit_price']= data['unit_price'].astype('float')

data["total_amount"] = data['quantity'] * data['unit_price']

data.head()

import pymysql
from sqlalchemy import create_engine
import psycopg2

data.to_csv('walmart_cleaned_csv.csv', index = False)

password = "Sarvesh@8767384243".replace("@", "%40")

engine_pgsql = create_engine(
    f'postgresql+psycopg2://postgres:{password}@localhost:5432/Project'
)

try:
    with engine_pgsql.connect() as conn:
        print("connection success to pgAdmin4")
except Exception as e:
    print("connection failed")
    print(e)

data.to_sql(name= 'walmart', con = engine_pgsql, if_exists = 'append', index = False)
