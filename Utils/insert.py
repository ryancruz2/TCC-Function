import psycopg2 as pg
import os
def insert_data_postgres(values):
    string = os.environ["ConnectionString"].split(";")
    with pg.connect(host=string[0],database=string[1],user=string[2],password=string[3]) as conn:
        with conn.cursor() as cursor:
            conn.close();