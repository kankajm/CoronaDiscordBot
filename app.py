import platform
import discord
from functions import misc_func
from dotenv import load_dotenv
from discord.ext import commands
from configparser import ConfigParser
from functions import commands_echo
import os

# load bot config
parser = ConfigParser()
parser.read('config.ini')
# loading env to os
load_dotenv()
# Default prefix of a command
client = commands.Bot(command_prefix='{}'.format(parser.get('INFO', 'command_prefix')))

@client.event
async def on_ready():
    print("Bot is online! Bot version: {}".format(parser.get('INFO', 'bot_version')))
    print("Discord.py version: " + discord.__version__)
    print("Server is running on " + misc_func.system_is() + ", Python version: " + platform.python_version())
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    activity = discord.Activity(name='{}'.format(parser.get('INFO', 'activity_name'))
                                , type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

@commands.command()
async def corona(ctx, args):
    if args in commands_echo.commands.getCzechPrefixes():
        await ctx.send(commands_echo.commands.getCzechCoronaData())
    if args in ['overview', 'world']:
        await ctx.send(ctx.message.author.mention + commands_echo.commands.getGlobalCoronaData())
    if args == "info":
        await ctx.send(ctx.message.author.mention + commands_echo.commands.getInfoAboutCoronavirus())
    if args == "help":
        embed = discord.Embed(title="Commands for the CoronaBot:", colour=discord.Color.red())
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        embed.set_footer(text="Created by Jaroslav Kaňka (kanka@jkanka.cz or kankaj#1973)",
                         icon_url="https://jkanka.cz/ikonka.png")
        embed.add_field(name="To show total numbers from countries all around the world use:",
                        value=".corona overview")
        embed.add_field(name="To show official numbers for the Czech Republic use:",
                        value=".corona czechia")
        embed.add_field(name="To show info and numbers about specific country use:",
                        value=".corona <country>")
        embed.add_field(name="To show verified info about symptoms of the COVID-19:",
                        value=".corona info")
        embed.add_field(name="To show version of the bot use:",
                        value=".corona version")
        embed.add_field(name="To show ping of the bot use:",
                        value=".corona ping")
        embed.add_field(name="To invite this bot on your server use:",
                        value=".corona invite")
        await ctx.send(embed=embed)
    if args == "ping":
        await ctx.send(f'Bots ping is {round(client.latency * 1000)}ms')
    if args == "invite":
        await ctx.send(ctx.message.author.mention + commands_echo.commands.getInviteLinkMessage())
    if args == "servers":
        guild_counter = 0
        for guild in client.guilds:
            guild_counter += 1
        await ctx.send("CoronaBot is on {} servers! Add him on your server too: https://shorturl.at/fprIN".format(guild_counter))
    if args == "version":
        await ctx.send('Bot version is: {}'.format(parser.get('INFO', 'bot_version')))
    if args == "S.Korea":
        await ctx.send(ctx.message.author.mention + commands_echo.commands.getKoreaFixedCoronaData())
    else:
        if args in commands_echo.commands.getIgnoredArgs():
            pass
        else:
            await ctx.send(ctx.message.author.mention + commands_echo.commands.getCountryCoronaData(args))

# Add command to the bot
client.add_command(corona)
# Getting env variable form os
SECRET_KEY = os.getenv("KEY")
# Imports key from secrets because of safety on Github
client.run(SECRET_KEY)
