import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils import BotUtils

bot = commands.Bot(command_prefix="FUCKING ")
load_dotenv(dotenv_path="token.env")
token = os.getenv('token')
utils = BotUtils(bot)
print(token)
killChannel = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def on_command_error(ctx):
    await ctx.send("fucking wrong command u stupid cunt")


@bot.command()
async def kill(ctx: commands.context.Context, user: discord.Member):
    global killChannel
    if killChannel is None:
        for i in ctx.guild.voice_channels:
            if i.id == 692176541022421012:
                killChannel = i
    try:
        await utils.moveUser(user, killChannel, "fuck you")
    except commands.errors.CommandInvokeError:
        await ctx.send(f"the user {user.display_name} is not connected to voice chat u stupid fuck")


bot.run(token)
