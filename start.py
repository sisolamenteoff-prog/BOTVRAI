import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
token = os.getenv("discord_token")


class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['moderation']:
            await self.load_extension(f'Cogs.{extension}')

intents = discord.Intents.all()
bot = MonBot(command_prefix="+", intents=intents)

keep_alive()
bot.run(token=token)