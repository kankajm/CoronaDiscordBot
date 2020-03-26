import logging
import os

def logger():
    # Creates logs
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(os.path.join('logs/data/', 'discord.log'))
    handler.setFormatter(logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)

