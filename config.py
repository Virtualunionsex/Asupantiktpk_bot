import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5835277295:AAHPYzLWOItoV8IJkp28jnkN_L-AI3Bd4Fw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001805757516"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1715348447"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://jdgqxjkz:i64ndEDX8WyLIrRigS38Izk-w64qA9SC@rosie.db.elephantsql.com/jdgqxjkz")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001606991843"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001528080636"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001569500029"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nPromo vvip dengan total 40K video lebih hanya 50K. hub @panggilaja_m")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5360457944").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Promo vvip 40K video lebih hanya 50K hub @panggilaja_m.<b>") 

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(1715348447)
ADMINS.append(5242442094) 
ADMINS.append(0) 

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
