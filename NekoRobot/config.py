# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/NekoRobot/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 17441778   # integer value, dont use ""
    API_HASH = "d221a3858d847abbec41da95840b4a64"
    TOKEN = "5926549446:AAGeZZBBGj_hvlbbtlIqfUnU7XzLDzYcjDM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    STRING_SESSION = ""
    MONGO_DB = "Shikimori"
    TEMP_DOWNLOAD_DIRECTORY= "./"
    MONGO_DB_URI = "mongodb+srv://toaa:toaa69@cluster0.eduoooo.mongodb.net/?retryWrites=true&w=majority"
    OWNER_ID = 1347884554  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "M_TOAA"
    HELP_IMG = "https://graph.org/file/1f3a67933a0d1d9135990.jpg"
    SUPPORT_CHAT = "scarletwitchsupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001676717902
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001676717902
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://gbjxuevv:2nl1aOrXO8cKC2xS742CAKE-5bKJJAfh@isilo.db.elephantsql.com/gbjxuevv"  # needed for any database modules
    DB_URI = "postgres://gbjxuevv:2nl1aOrXO8cKC2xS742CAKE-5bKJJAfh@isilo.db.elephantsql.com/gbjxuevv"
    REDIS_URL = "redis://default:6vsajwd6wq3lNI7T3zMIpltTrU040DJC@redis-19248.c16.us-east-1-3.ec2.cloud.redislabs.com:19248"
    LOAD = []
    BOT_USERNAME = "Scarlett_Witchh_Bot"
    ARQ_API_URL = "arq.hamker.dev"
    ARQ_API_KEY = "DYIEDF-OHGOYY-UHZTFX-HXDDAU-ARQ"
    ERROR_LOGS = -1001813334646
    BOT_NAME = "Scarlet Witch"
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    REM_BG_API_KEY = "PxCe5v4ZX3RmoQnPdDzf2TTz"
    SPAMWATCH_API = "QsrtejDpiLrvimOWSQeq6hpLNyMI_RIA_TfKExdSnBKE20I2gIXeDxBxYC76kLE6"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "VQ45LFKYPMJ2LKIU"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "65G8ZKE6050P"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "SOME1HING_privet_990022"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True  # Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
