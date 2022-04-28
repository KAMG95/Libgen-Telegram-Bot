import os
import logging

# mode = "prod" for heroku "dev" for running locally

mode = "prod" 
TELEGRAM_ACCESS_TOKEN = "5349903888:AAGhbsTC5dPW04nFX2x-9hk-nDgQzukL9Fk"
HEROKU_APP_NAME = "libgenzerodawn"
LIBGEN_DOMAIN = "https://libgen.is/"

# Enable logging
logging.basicConfig(format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
