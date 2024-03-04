# TODO - CALCULATOR OR Using external online services for calculation with certain commands
# /calc # or /calculate #
# /history - shows latest 5 calculations in a history
# /clear - clearup the history

import discord
from discord.ext import commands

class Calculator(commands.Cog):
    def __int__(self,client):
        self.client = client

    # create a set of functions that will provide the necessary operations.



def setup(client):
    client.add_cog(Calculator(client))