import nextcord
from nextcord.ext import commands
import os

class TestingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # create a set of functions that will provide the necessary operations.

    @commands.command(name="test", description="Run a test")
    async def test_command(self, ctx):
        await ctx.send("This is a test command.")

    @commands.command(name="ping", description="Check internet connectivity")
    async def ping_command(self, ctx):
        response = os.system("ping -c 1 google.com")
        if response == 0:
            await ctx.send("Internet is reachable.")
        else:
            await ctx.send("Internet is not reachable.")

def setup(bot):
    bot.add_cog(TestingCog(bot))
