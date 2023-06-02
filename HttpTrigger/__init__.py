import logging
from Utils.insert import insert_data_postgres
from Utils.request import get_phones
import azure.functions as func
from Utils.tratament import get_values_json
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Captura iniciada')
    phones = get_phones()

    if(type(phones) == str):
        return func.HttpResponse(
             phones,
             status_code=400
        )
    else:
        phones = get_values_json(phones)
        insert_data_postgres(phones)
        return func.HttpResponse(
            body=json.dumps(phones),
            status_code=200,
            mimetype='application/json'
        )