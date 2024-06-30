HEROKU = True  #

# 
if HEROKU:
    from os import environ

    Bot_token = environ["Bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# 
if not HEROKU:
    Bot_token = "7264691572:AAFRSbLlqSQJggpKrTsmkgJaEhsokrlYrys"
    ARQ_API_KEY = "VBZRUJ-YNTKMN-ISNOJM-ATSYPU-ARQ"
