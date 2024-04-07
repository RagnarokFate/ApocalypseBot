import nextcord
from nextcord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hi", description="Says hi with a special message")
    async def hi_command(self, ctx):
        await ctx.channel.send("Hi there! I'm here to assist you.")

    @commands.command(name="setstatus", description="Sets bot status")
    async def set_status_command(self, ctx, status: str):
        await self.bot.change_presence(activity=nextcord.Game(name=status))

def setup(bot):
    bot.add_cog(AdminCog(bot))
