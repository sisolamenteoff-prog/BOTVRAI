import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="+", intents=intents)


@bot.command()
async def hello_world(context):
  await context.reply("Hello, world!")


@bot.command(
    description="Commence un timer",
    brief="Decompte d'un nombre a 0",
    help="Encore plus d'aide"

)
async def decompte(context, delai: int):
  await context.send("Départ dans ...")
  for i in range(delai, 0, -1):
    await context.send(i)
  await context.send("C'est parti !")


@bot.command(
    description="Repete ce qu'on lui dit",
    brief="Repete tout",
    help="Encore plus d'aide"
)
async def repeter(context, *, message):
    await context.send(message)

if __name__ == '__main__': 
 bot.run("MTQ0Njg3MzgzOTU4NDgwNTA0NQ.GYwAix.13DucZgsZrVVT_mb9fXl5HRJCgXd9liu5rmIYU")