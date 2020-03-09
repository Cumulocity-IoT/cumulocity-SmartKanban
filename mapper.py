import jsonify
import csv
import pandas
import logging
import requests
import settings
from base64 import b64encode

logger = logging.getLogger('Mapper')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.debug('Logger for Mapper was initialised')
payload = {}
headers = {"Authorization": "Basic {}".format(b64encode(bytes(f"{settings.c8yUser}:{settings.c8yPassword}", "utf-8")).decode("ascii"))}
def checkWhetherIDIsListed(ID):
    logger.info('Checking against indentity service whether ID is valid in C8Y')
    url = "https://" + settings.tenant + "/identity/externalIds/c8y_Serial/" + str(ID)
    response = requests.request("GET", url, headers=headers, data = payload)
    if response.status_code == 200:
        logger.info('Mac Address exists in C8Y')
        return True
    else:
        print("No")
        return False
