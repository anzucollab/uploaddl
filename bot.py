#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ENV = bool(os.environ.get('ENV', False))
try:
  if ENV:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    APP_ID = os.environ.get('APP_ID')
    API_HASH = os.environ.get('API_HASH')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    SUDO_USERS = os.environ.get('SUDO_USERS')
    SUPPORT_CHAT_LINK = os.environ.get('SUPPORT_CHAT_LINK', 'https://t.me/ViperCommunity')
    DOWNLOAD_DIRECTORY = os.environ.get("DOWNLOAD_DIRECTORY", "./downloads/")
  else:
    from bot.config import config
    BOT_TOKEN = config.BOT_TOKEN
    APP_ID = config.APP_ID
    API_HASH = config.API_HASH
    DATABASE_URL = config.DATABASE_URL
    SUDO_USERS = config.SUDO_USERS
    SUPPORT_CHAT_LINK = config.SUPPORT_CHAT_LINK
    DOWNLOAD_DIRECTORY = config.DOWNLOAD_DIRECTORY
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AnyDLBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
        parse_mode="markdown",
        workdir=DOWNLOAD_DIRECTORY
    )
    Config.AUTH_USERS.add(7351948)
    app.run()
