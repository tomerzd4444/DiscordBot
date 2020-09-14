import os

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from utils import BotUtils

bot = commands.Bot(command_prefix="FUCKING ")
load_dotenv(dotenv_path="token.env")
token = os.getenv('token')
utils = BotUtils(bot)
print(token)
killChannel = None


@bot.event
async def on_member_join(member: discord.Member):
		role = get(member.server.roles, id=705761329901994015)
		await bot.add_roles(member, role)
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


@bot.command()
async def ban(ctx: commands.context.Context, user: discord.Member):
	if user.id == 306114855063257099:
		await ctx.send("u can not ban that user u fuck")
		await ctx.guild.ban(ctx.message.author, reason="you tried to ban blueblood u fuck")
		return
	await ctx.guild.ban(user,reason="fuck u")
	await ctx.send(f"banned the user {user.display_name} cause fuck u")

bot.run(token)
