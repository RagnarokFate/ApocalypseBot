import discord
from discord.ext import commands


banner_path = "images/banner_image.jpeg"
class In_Out(commands.Cog):
    def __int__(self, client):
        self.client = client

    # create a set of functions that will provide the necessary operations.
    @commands.command(name="hello")
    async def hello(self,ctx):
        await ctx.send("Hello there, I'm ApocalypseBot created by RagnarokFate")

    @commands.Cog.listeners(name="on_member_join")
    async def on_member_join(self,member):
        welcome_channel = member.guild.system_channel
        file = discord.discord.File(banner_path)
        await welcome_channel.send(f"Welcome {member.mention} to the server!", file=discord.File(banner_path))

    @commands.Cog.listeners(name="on_member_remove")
    async def on_member_remove(self,member):
        goodbye_channel = member.guild.system_channel

        if goodbye_channel:
            await goodbye_channel.send(f"Goodbye {member.display_name}! We'll miss you.")
def setup(client):
    client.add_cog(In_Out(client))