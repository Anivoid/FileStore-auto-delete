#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6367580975:AAGGo8EUjgUWKnNrCAXou0_Ua86rvVednog")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20263428"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f9dc42564f6e6eb9920912b09f729e3f")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001988634929"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Ariesaep")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7102263732"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Anivoid:akhand1616@cluster05.kzyifsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster05")
DB_NAME = os.environ.get("DATABASE_NAME", "AiFileShare")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002154284624"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002154284624"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e8e25e73d7a1ee6dfba98.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/e8e25e73d7a1ee6dfba98.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Ariesaep\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Ariesaep>Akki</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Ariesaep>Akki</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/ongoing_haniflix>Haniflix network</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/animesilvervoid>Silvervoid [ℍ𝕌𝔹]</a>\n◈  Movie Channel : <a href=https://t.me/silvervoidmovie>Silvervoid [𝕄𝕠𝕧𝕚𝕖]</a>\n◈ Javflix : <a href=https://t.me/+_klqs93gEstkYzk1>Javflix</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Ariesaep>Akki</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}\n\n I'am file store bot of @Ariesaep! 📁✨\nʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ❗try:.</b>")
try:
    ADMINS=[7102263732]
    for x in (os.environ.get("ADMINS", "1582227872 6095034047").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @ongoing_haniflix</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "true") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(7102263732)

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
   
