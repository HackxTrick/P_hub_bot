HEROKU = True  #

# 
if HEROKU:
    from os import environ

    BOT_TOKEN = environ["Bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# 
if not HEROKU:
    BOT_TOKEN = "Insert Bot_Token Here"
    ARQ_API_KEY = "Get this from @ARQRobot"
