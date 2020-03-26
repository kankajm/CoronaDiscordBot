import discord
import logging
from functions import api_func
from functions import misc_func
from logs import logging
from dotenv import load_dotenv
import os

# loading env to os
load_dotenv()
# geting env variable form os
SECRET_KEY = os.getenv("KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        misc_func.debug_bot_onstart(self.user)
        # Starts making logs
        logging.logger()
        # Basic discord presence OUTPUT: Watching for your health ♥
        activity = discord.Activity(name='For your health ' + '♥', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!corona'):
            user = message.author
            data = api_func.api.overview_corona()
            await message.channel.send("{}, there's {} cases right now, {} deaths and {} people recovered from the COVID-19."
                                       .format(user, data[0], data[1], data[2]))

client = MyClient()
# Imports key from secrets because of safety on Github
client.run(SECRET_KEY)
