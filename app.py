import platform
import discord
from functions import api_func
from functions import misc_func
from dotenv import load_dotenv
from discord.ext import commands
from configparser import ConfigParser
from functions.scraping import mzcr_data as mzcr
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
    # Gives info about the Czech Republic
    if country_userinput == "CZ" or country_userinput == "cz" or country_userinput == "czech" or country_userinput == "czechia" or country_userinput == "Czechia" or country_userinput == "Czech":
        data = mzcr.covid_scrap()
        data_two = api_func.api.country_corona("Czechia")
        first_case = data_two[10].rstrip(" ")
        await ctx.send(f'According to Ministry of Health of the Czech Republic, Czechia has tested {data[2]} people. To this date Czechia have {data[3]} cases,'
                       f' {data[5]} deaths and {data[4]} people recovered from the COVID-19. First case was detected on {first_case}. Source: http://tiny.cc/mzcr-covid , {data[0]}.')
    else:
        # .corona overview prints overview about the situation
        if country_userinput == "overview" or country_userinput == "world":
            data = api_func.api.overview_corona()
            await ctx.send(f"{ctx.message.author.mention}, there's {data[0]} cases in a world right now, {data[1]} deaths and {data[2]} people recovered from the COVID-19.")
        else:
            # Gives info about the symptoms of the COVID-19
            if country_userinput == "info":
                info = misc_func.symptoms_info()
                await ctx.send(f"{ctx.message.author.mention}, {info} Source: http://tiny.cc/WHOLINK , WHO")
            else:
                # Shows all the possible commands for this bot
                if country_userinput == "help":
                    embed = discord.Embed(title="Commands for the CoronaBot:", colour=discord.Color.red())
                    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
                    embed.set_footer(text="This bot is proudly written in the Czech Republic by Jaroslav Kaňka and Ondřej Štěch.", icon_url="https://jkanka.cz/ikonka.png")

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
                else:
                    # .corona ping prints out ping of connection to Dicord API
                    if country_userinput == "ping":
                        await ctx.send(f'Bots ping is {round(client.latency * 1000)}ms')
                    else:
                        # Sends invite link to add CoronaBot on their server
                        if country_userinput == "invite":
                            invite_link = parser.get('INFO', 'invite_link')
                            await ctx.send(f'{ctx.message.author.mention}, to invite this bot on your server use: {invite_link}')
                        else:
                            # Special command for South Korea because of their name in the API ("S. Korea" can't be used in one parameter command)
                            if country_userinput == "S.Korea":
                                data = api_func.api.country_corona("S. Korea")
                                await ctx.send(f"{ctx.message.author.mention}"
                                               f", {data[0]} has {data[1]} cases and {data[3]} deaths. Today there are {data[2]} cases and {data[4]} deaths. {data[5]} people recovered."
                                               f" They're still {data[6]} active cases and {data[7]} people are in critical condition."
                                               f" The concentration of cases in {data[0]} is {data[8]} cases per one milion citizens. First case was recognized on {data[10]}.")
                            else:
                                # .corona version prints out version number
                                if country_userinput == "version":
                                    await ctx.send('Bot version is: {}'.format(parser.get('INFO', 'bot_version')))
                                else:
                                    # .corona <COUNTRY> prints out info about a single country of choice
                                    data = api_func.api.country_corona(country_userinput)
                                    if data == "error":
                                        await ctx.send(
                                            "You have written wrong country name or database is unavaible. Try it again.")
                                    else:
                                        await ctx.send(f"{ctx.message.author.mention}"
                                                       f", {data[0]} has {data[1]} cases and {data[3]} deaths. Today there are {data[2]} cases and {data[4]} deaths. {data[5]} people recovered."
                                                       f" They're still {data[6]} active cases and {data[7]} people are in critical condition."
                                                       f" The concentration of cases in {data[0]} is {data[8]} cases per one milion citizens. First case was recognized on {data[10]}.")


# Getting env variable form os
SECRET_KEY = os.getenv("KEY")
# Imports key from secrets because of safety on Github
client.run(SECRET_KEY)
