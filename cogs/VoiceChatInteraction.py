import discord
import youtube_dl
from discord.ext import commands

class VoiceChatInteraction(commands.Cog):
    def __init__(self, client):
        self.client = client

    # create a set of functions that will provide the necessary operations.
    # ================================== VOICE CHAT ====================================================
    @commands.command(pass_context=True)
    async def join(self, ctx):
        print("Joining a voice chat")
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

    @commands.command(pass_context=True)
    async def disconnect(self, ctx):
        print("Leaving a voice chat")
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

    @commands.command(pass_context=True)
    async def test(self, ctx):
        # Import necessary libraries
        import time
        import requests

        # Calculating bot's latency
        latency = round(self.client.latency * 1000)

        # Checking internet connection by sending a request to google.com
        start_time = time.time()
        try:
            requests.get('http://google.com')
            end_time = time.time()
            internet_latency = round((end_time - start_time) * 1000)
            await ctx.send(f'Bot Latency: {latency}ms\nInternet Latency: {internet_latency}ms')
        except requests.ConnectionError:
            await ctx.send('No internet connection.')

    @commands.command(name='play', help='Plays music in a voice channel')
    async def play(self, ctx, url):
        channel = ctx.author.voice.channel
        voice_channel = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        with youtube_dl.YoutubeDL({}) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']

        voice_channel.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))

    @commands.command(name='stop', help='Stops playing music and disconnects the bot')
    async def stop(self, ctx):
        voice_channel = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_channel.is_playing():
            voice_channel.stop()
        await voice_channel.disconnect()

def setup(client):
    client.add_cog(VoiceChatInteraction(client))
