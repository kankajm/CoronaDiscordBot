import platform
import discord
from functions import api_func
from functions import misc_func
from dotenv import load_dotenv
from discord.ext import commands
from configparser import ConfigParser
import os

# load bot config
parser = ConfigParser()
parser.read('config.ini')
# loading env to os
load_dotenv()
# Default prefix of a command
client = commands.Bot(command_prefix='{}'.format(parser.get('INFO', 'command_prefix'))
                      , case_insensitive=True)

@client.event
async def on_ready():
    print("Bot Online! Bot version: {}".format(parser.get('INFO', 'bot_version')))
    print("Discord.py version: " + discord.__version__)
    print("Server is running on " + misc_func.system_is() + ", Python version: " + platform.python_version())
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    activity = discord.Activity(name='{}'.format(parser.get('INFO', 'activity_name'))
                                , type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

# TODO: Error message if it's without value
@client.command()
async def corona(ctx, country_userinput):
        # .corona overview prints overview about the situation
        if country_userinput == "overview":
            data = api_func.api.overview_corona()
            await ctx.send(f"{ctx.message.author.mention}, there's {data[0]} cases in a world right now, {data[1]} deaths and {data[2]} people recovered from the COVID-19.")
        else:
            # .corona ping prints out ping of connection to Dicord API
            if country_userinput == "ping":
                await ctx.send(f'Bots ping is {round(client.latency * 1000)}ms')
            else:
                # .corona version prints out version number
                if country_userinput == "version":
                    await ctx.send('Bot version is: {}'.format(parser.get('INFO', 'bot_version')))
                else:
                    # .corona <COUNTRY> prints out info about a single country of choice
                    data = api_func.api.country_corona(country_userinput)
                    if data == "error":
                        await ctx.send("You have written wrong country name or database is unavaible. Try it again.")
                    else:
                        await ctx.send(f"{ctx.message.author.mention}"
                                       f", {data[0]} has {data[1]} cases and {data[3]} deaths. Today there are {data[2]} cases and {data[4]} deaths. {data[5]} people recovered."
                                       f" They're still {data[6]} active cases and {data[7]} people are in critical condition."
                                       f" The concentration of cases in {data[0]} is {data[8]} cases per one milion citizens. First case was recognized on {data[10]}.")

# Getting env variable form os
SECRET_KEY = os.getenv("KEY")
# Imports key from secrets because of safety on Github
client.run(SECRET_KEY)
