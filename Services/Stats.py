import discord
from discord.ext import commands

class Stats(commands.Cog):
    def __int__(self,client):
        self.client = client

    # create a set of functions that will provide the necessary operations.



def setup(client):
    client.add_cog(Stats(client))