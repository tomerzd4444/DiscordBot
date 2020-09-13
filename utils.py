import discord
from discord.ext import commands


class BotUtils:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def moveUser(self, user: discord.Member, channel: discord.VoiceChannel, reason: str = None):
        return user.move_to(channel, reason=reason)
