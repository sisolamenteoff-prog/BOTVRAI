import discord
from discord.ext import commands


class ModCogs(commands.Cog):
  def __init__(self, bot) :
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send(f"{member.name} a été exclu(e).")

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f"{member.name} a été banni")

async def setup(bot):
    await bot.add_cog(ModCogs(bot))
