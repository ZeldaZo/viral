# (©)Codexbotz
# Recode by @kang_culiknee


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6435245106:AAEvWrQPsDGUne2zfnmOK4fM9-eZI_hU8sY")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9774346"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "a92aed7d74654a563af4b07efbcd88e9")

# ID Channel Databas
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002108420285"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "968410597"))

# NAMA OWNER
OWNER = os.environ.get("OWNER","MafiaYakuza")

# Databasenya 
DB_URI = os.environ.get("DATABASE_URL", "postgres://tezuycqi:28iQ60s-vnijaBq_3ZN-bvgmyq4V6Ppl@bubble.db.elephantsql.com/tezuycqi")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Zoids_Robot")
GROUP = os.environ.get("GROUP", "Zoidssupport")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL","-1001507337802"))

FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1002091796126"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus @Zoids_Robot.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6349534788").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu\n\n@Zoids_Robot</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", True) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(968410597)
ADMINS.append(968410597)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
