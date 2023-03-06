import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5852106103:AAEFt4Ln3NNu5uAI-iJWd34-t6n631Tmg5g")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001756470619"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5680450278"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://rwgmydpn:1s_ykVlSf3iZ-eznaY3Ke8I8iDYxdG9d@batyr.db.elephantsql.com/rwgmydpn")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001861704447"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001815711149"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001569500029"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\npromo vvip 9 grup total puluhan ribu video dengan harga 50K. Hub @panggilaja_m.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1908660708 5680450278 1715348447").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nJOIN VVIP MURAH DAN TERPERCAYA 50K SUDAH DAPAT 9 GRUP/CHANNEL DENGAN TOTAL VIDEO PULUHAN RIBU </b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(5680450278)
ADMINS.append(1908660708)

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
