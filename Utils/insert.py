import psycopg2 as pg
import os
import logging
def format_values(value: dict):
    return tuple(value.values())

def insert_data_postgres(values: list[dict] ):
    data = [
        list(map(lambda x: x["id"] , values)),
        list(map(lambda x: x["name"] , values)),
        list(map(lambda x: x["maker"] , values)),
        list(map(lambda x: x["image"] , values)),

    ]
    string = os.environ["ConnectionString"].split(";")
    try:
        with pg.connect(host=string[0],database=string[1],user=string[2],password=string[3]) as conn:
            with conn.cursor() as cursor:
                logging.info("Iniciando Inserção")
                query = "INSERT INTO \"Phones\" (id,name,maker,image) VALUES (UNNEST(%s),UNNEST(%s),UNNEST(%s),UNNEST(%s))"
                cursor.execute(query,data)
                conn.commit()
                cursor.close()
            conn.close()
            logging.info("Dados Inseridos no Postgres com sucesso")
            logging.info("Iniciando inserção no elastic Search")
            return;
    except:

        return;


