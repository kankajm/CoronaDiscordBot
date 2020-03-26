import discord
import logging
from functions import api_func
from functions import misc_func
from logs import logging
from dotenv import load_dotenv
from discord.ext import commands
import os

# Bot version
bot_version = "1.0"
# loading env to os
load_dotenv()
# geting env variable form os
SECRET_KEY = os.getenv("KEY")
# Default prefix of a command
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot Online!")
    print("Discord.py version: " + discord.__version__)
    print("Server is running on " + misc_func.system_is())
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    activity = discord.Activity(name='.corona <country>', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

@client.command()
async def ping(ctx):
    await ctx.send(f'DEBUG: Ping is {round(client.latency * 1000)}ms')

@client.command()
async def version(ctx):
    await ctx.send(f'Bot version is: {bot_version}')

@client.command()
async def coronaoverview(ctx):
    data = api_func.api.overview_corona()
    await ctx.send(f"{ctx.message.author.mention}, there's {data[0]} cases right now, {data[1]} deaths and {data[2]} people recovered from the COVID-19.")

# TODO: Make parameter --details
# TODO: Error message if it's without value
@client.command()
async def corona(ctx, country_userinput):
        data = api_func.api.country_corona(country_userinput)
        if data == "error":
            await ctx.send("You have written wrong country name or database is unavaible.")
        else:
            await ctx.send(
                f"{ctx.message.author.mention}, {data[0]} have {data[1]} cases and {data[3]} deaths. Today there are {data[2]} cases and {data[4]} deaths. {data[5]} people recovered.")

# Imports key from secrets because of safety on Github
client.run(SECRET_KEY)
