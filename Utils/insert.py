import psycopg2 as pg
import os
import logging
import requests as req

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
    
    with pg.connect(host=string[0],database=string[1],user=string[2],password=string[3]) as conn:
        with conn.cursor() as cursor:
            logging.info("Iniciando Inserção")
            query = "INSERT INTO \"Phones\" (id,name,maker,image) VALUES (UNNEST(%s),UNNEST(%s),UNNEST(%s),UNNEST(%s)) ON CONFLICT DO NOTHING"
            cursor.execute(query,data)
            conn.commit()
            cursor.close()
        conn.close()
        logging.info("Dados Inseridos no Postgres com sucesso")
        logging.info("Iniciando inserção no elastic Search")
        insert_elastic_search(values)
        return;

def create_model_json(json):
    return {
        "@search.action": "mergeOrUpload",
        "id": str(json["id"]),
        "name": json["name"],
        "maker": json["maker"],
        "image": json["image"]
    }

def insert_elastic_search(data):
    data = list(map(create_model_json, data))

    url = os.environ["UrlSearch"]
    index = os.environ["IndexSearch"]
    res = req.post(f"{url}/indexes/{index}/docs/index?api-version=2021-04-30-preview", headers={"api-key": os.environ["TokenSearch"]}, json={"value": data}).json()
    logging.info("dados inseridos com sucesso");
    return;
