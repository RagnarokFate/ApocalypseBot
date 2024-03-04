import discord
from discord.ext import commands

class Student(commands.Cog):
    def __int__(self,client):
        self.client = client

    # create a set of functions that will provide the necessary operations.



def setup(client):
    client.add_cog(Student(client))