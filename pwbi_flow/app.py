from pwbi_flow.ETL.extract import *
from pwbi_flow.ETL.load import *
import pandas as pd


def run():

    #ENTER YOUR DAX QUERY BELLOW

    query = "EVALUATE('DATASET NAME OR COLUMS HERE')"

    #ENTER A NAME FOR YOUR TABLE TO BE USED TO UPLOAD THE FILE TO S3

    table_name = 'your_data'

    data = extract_data(table_name, query)

    data.to_csv(f'{table_name}.csv')

    push_datalake(table_name, data, 'pwbi')

try:
    run()
except Exception as e:
    print(f"An error occurred: {e}")
