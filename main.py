import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="FUCKING ")
load_dotenv(dotenv_path="token.env")
token = os.getenv('token')
print(token)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def on_command_error(ctx):
    await ctx.send("fucking wrong command u stupid cunt")


@bot.command()
async def kill(ctx: commands.context.Context, user: discord.Member):
    print(type(ctx))
    await ctx.send(f"fuck u {user.display_name}")



bot.run(token)
