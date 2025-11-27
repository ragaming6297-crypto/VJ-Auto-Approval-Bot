# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("32800034", ""))
    API_HASH = getenv("0a0048d9d90399a4b2b1cc44ab1c27a6", "")
    BOT_TOKEN = getenv("8433346180:AAEeltpcu7-_LLUan1ERa7rx_KI3LwcdvzI", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("mongodb+srv://sureshffconfigs:sk0811@cluster0.c50m0da.mongodb.net/?appName=Cluster0", "")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
