# Burada jwt token kontrolü yapılacak gelen tüm requestler kontrol edilecek.
# requestler loglanması gerekirse... Flask'ın logging kullanılabilir
import logging
from flask import request_started

def requestFilter(sender, **extra):
    # Loggin nereye logluyor bilemedim docs
    # https://flask.palletsprojects.com/en/2.2.x/logging/
    logging.info('Started')
    print('Request start!')

