import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Captura iniciada')
    return func.HttpResponse(
             "",
             status_code=200
        )
