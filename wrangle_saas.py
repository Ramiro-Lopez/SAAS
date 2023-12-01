import env
import os
import pandas as pd
import numpy as np 

from sklearn.model_selection import train_test_split

# Wrangle functions for Zillow Data 

def get_connection(db: str, user: str = env.user, host: str = env.host, password=env.password) -> str: 
    '''
       This function takes in a data base, username, password, and hoast from MySQL
       and returns a my url as a string
    '''
    return f"mysql+pymysql://{user}:{password}@{host}/{db}"

def get_churn_data(file_name="churn.csv") -> pd.DataFrame: # add to wrangle file 
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    query = """select * from churn;
            """
    connection = get_connection("saas_llc")
    df = pd.read_sql(query, connection)
    df.to_csv(file_name, index=False)
    return df

# parse_dates=['transactiondate'] droped but might need it ß