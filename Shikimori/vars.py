import os


ENV = bool(os.environ.get("ENV", True))

if ENV:
    TOKEN = os.environ.get("BOT_TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", "5001899507"))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
     
    ERROR_LOG_CHANNEL = os.environ.get("ERROR_LOG_CHANNEL", "-1001668540922")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Mr_nack_nack")

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "5001899507").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "5001899507").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "5001899507").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "5001899507").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "5001899507").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001668540922")
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", "12910042")
    API_HASH = os.environ.get("API_HASH", "31201ad2becae3dc8e1e55f9ae294cb9")
    DB_URL = os.environ.get("DATABASE_URL", "postgres://nslschmo:s_JMh5gRYKFZGl34GngpaHUi2_R-bBxm@peanut.db.elephantsql.com/nslschmo")
    DB_URL = DB_URL.replace("postgres://nslschmo:s_JMh5gRYKFZGl34GngpaHUi2_R-bBxm@peanut.db.elephantsql.com/nslschmo", "postgres://nslschmo:s_JMh5gRYKFZGl34GngpaHUi2_R-bBxm@peanut.db.elephantsql.com/nslschmo", 1)
    FUNC_DB_URL = os.environ.get("FUNC_DB_URL", "postgres://nslschmo:s_JMh5gRYKFZGl34GngpaHUi2_R-bBxm@peanut.db.elephantsql.com/nslschmo")
    FUNC_DB_URL = FUNC_DB_URL.replace("postgres://nslschmo:s_JMh5gRYKFZGl34GngpaHUi2_R-bBxm@peanut.db.elephantsql.com/nslschmo", "postgres://nslschmo:s_JMh5gRYKFZGl34GngpaHUi2_R-bBxm@peanut.db.elephantsql.com/nslschmo", 1)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://ub:ub123@horivc.cemtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    ARQ_API = os.environ.get("ARQ_API_BASE_URL", "BMUXJR-WMSSAL-QEXJPP-AHNYFN-ARQ")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", None).split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", True)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", "-xyz")
    AI_API_KEY = os.environ.get("AI_API_KEY", "SOME1HING_privet_990022")
    API_WEATHER = os.environ.get("API_WEATHER", "a4d26025620a9902fce9c89996b10495")
    WALL_API = os.environ.get("WALL_API", "6950f5ds6a3")
    REDIS_URL = os.environ.get("REDIS_URL", "redis://default:9pmhTFvTxV2LVx9rzuTO@containers-us-west-133.railway.app:6851")
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "gojo_support")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    ARQ_API_KEY = os.environ.get("ARQ_API", "BMUXJR-WMSSAL-QEXJPP-AHNYFN-ARQ")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "gojobot7")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "37c5470e-7b72-45c4-829f-395a2d83b760")
    APOD_API_KEY = os.environ.get("APOD_API_KEY", "ITDcBLGdFJt5h2zv9Bbm3lLCg4q3PEAK8YhfZ5HW")
    ANIME_NAME = os.environ.get("ANIME_NAME", "Jᴜᴊᴜᴛsᴜ Kᴀɪsᴇɴ")
    START_MEDIA = os.environ.get("START_MEDIA", "https://telegra.ph/file/f2d390bad48ee15c36011.mp4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Gojoa_satoru_bot")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "gojo_bot_updates")
    ALIVE_MEDIA = os.environ.get("ALIVE_MEDIA", "https://telegra.ph/file/a6c30cd075df16dae7bb5.mp4")
    BOT_ID = int(os.environ.get("BOT_ID", "5484116052"))
    STATS_IMG = os.environ.get("STATS_IMG", "https://telegra.ph/file/1f5aa2587aace405edca8.jpg")
    NETWORK = os.environ.get("NETWORK", "【V๏ɪ፝֟𝔡】»Network«")
    NETWORK_USERNAME = os.environ.get("NETWORK_USERNAME", "VoidxNetwork")
    MEDIA_GM = os.environ.get("MEDIA_GM", "https://telegra.ph/file/a6c30cd075df16dae7bb5.mp4")
    MEDIA_GN = os.environ.get("MEDIA_GN", "https://telegra.ph/file/bfe511a9f3b1bf225c144.mp4")
    MEDIA_HELLO = os.environ.get("MEDIA_HELLO", None)
    MEDIA_BYE = os.environ.get("MEDIA_BYE", "https://telegra.ph/file/bfe511a9f3b1bf225c144.mp4")
    INLINE_IMG = os.environ.get("INLINE_IMG", "https://telegra.ph/file/1f5aa2587aace405edca8.jpg")
    OWNER_WELCOME_MEDIA = os.environ.get("OWNER_WELCOME_MEDIA", "https://telegra.ph/file/d0212e969f6b1f042d57d.jpg")

    try:
        WHITELIST_CHATS = {int(x) for x in os.environ.get('WHITELIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

    try:
        BLACKLIST_CHATS = {int(x) for x in os.environ.get('BLACKLIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

else:
    from Shikimori.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")
    ERROR_LOG_CHANNEL = Config.ERROR_LOG_CHANNEL
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    LOG_CHANNEL = Config.LOG_CHANNEL
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    HEROKU_API_KEY = Config.HEROKU_API_KEY
    HEROKU_APP_NAME = Config.HEROKU_APP_NAME
    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    API_WEATHER = Config.API_WEATHER
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    APOD_API_KEY = Config.APOD_API_KEY
    REDIS_URL = Config.REDIS_URL
    ANIME_NAME = Config.ANIME_NAME
    START_MEDIA = Config.START_MEDIA
    BOT_USERNAME = Config.BOT_USERNAME
    UPDATE_CHANNEL = Config.UPDATE_CHANNEL
    ALIVE_MEDIA = Config.ALIVE_MEDIA
    BOT_ID = Config.BOT_ID
    STATS_IMG = Config.STATS_IMG
    NETWORK = Config.NETWORK
    NETWORK_USERNAME = Config.NETWORK_USERNAME
    MEDIA_GM = Config.MEDIA_GM
    MEDIA_GN = Config.MEDIA_GN
    MEDIA_HELLO = Config.MEDIA_HELLO
    MEDIA_BYE = Config.MEDIA_BYE
    INLINE_IMG = Config.INLINE_IMG
    OWNER_WELCOME_MEDIA = Config.OWNER_WELCOME_MEDIA

    try:
        WHITELIST_CHATS = {int(x) for x in os.environ.get('WHITELIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

    try:
        BLACKLIST_CHATS = {int(x) for x in os.environ.get('BLACKLIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")
            
PM_START_TEXT = """
\nɪ ᴀᴍ *{Bot_name}*, ᴀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴍᴇɴᴛ ʙᴏᴛ ʙᴀsᴇᴅ ᴏɴ ᴛʜᴇ ᴀɴɪᴍᴇ *{ANIME_NAME}*![ ]({START_MEDIA})
*★━━━━━━━━━━━━━━━━━━━━★
ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ! ʜɪᴛ /help ᴛᴏ ꜰɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴛᴏ ᴍʏ ꜰᴜʟʟ ᴘᴏᴛᴇɴᴛɪᴀʟ. ✦
★━━━━━━━━━━━━━━━━━━━━★.*
"""

HELP_STRINGS = """
𝙲𝚕𝚒𝚌𝚔 𝚘𝚗 𝚝𝚑𝚎 𝚋𝚞𝚝𝚝𝚘𝚗 𝚋𝚎𝚕𝚕𝚘𝚠 𝚝𝚘 𝚐𝚎𝚝 𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚜𝚙𝚎𝚌𝚒𝚏𝚒𝚌𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍."""
