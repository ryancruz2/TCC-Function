import requests as req
import os

def get_phones():
    response = req.get(os.environ["ApiInfoCellPhone"])
    if response.status_code == 200:
        return response.json()[1]
    else:
        return "Faild request api"
    