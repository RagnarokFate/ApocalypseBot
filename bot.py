import discord
from discord.ext import commands
import responses
import values
import time
import requests
from discord.utils import get
import youtube_dl
import asyncio
import re


def run_discord_bot():
    intents = discord.Intents.default()  # Create a default set of intents
    intents.message_content = True
    intents.members = True
    client = commands.Bot(command_prefix='/',intents=intents)
    stopwatch_channel_name = "stopwatch"
    reminder_channel_name = "reminders"

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        server = ""
        try:
            if message.guild != None:
                server = str(message.guild.name)
        except Exception as e:
            print(e)

        # INPUT CHECK PRINT
        if server == "":
            print(f"{username} | '{user_message}' | '{channel}'")
        else :
            print(f"{username} | '{user_message}' | '{channel}' | '{server}'")

        # RESPONSE INTERACTION
        # strip remove extra spaces and organize command to straight forward format.
        if user_message.strip():
            # Direct Message Bot Commands
            if user_message[0] == '!':
                user_message = user_message[1:]
                # Status = user
                await responses.sent_message(message,user_message,is_private=True)
            # Server Message Bot Commands
            elif user_message[0] == '/':
                user_message = user_message[1:]
                # Status = non-user (more of community term)
                await responses.sent_message(message,user_message,is_private=False)
        else:
            print("User's message is empty or contains only whitespace.")

        await client.process_commands(message)

    # ================================== VOICE CHAT ====================================================
    @client.command(pass_context=True)
    async def join(ctx):
        print("Joining a voice chat")
        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

    @client.command(pass_context=True)
    async def disconnect(ctx):
        print("Leaving a voice chat")
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

    @client.command(pass_context=True)
    async def test(ctx):
        # Calculating bot's latency
        latency = round(client.latency * 1000)

        # Checking internet connection by sending a request to google.com
        start_time = time.time()
        try:
            requests.get('http://google.com')
            end_time = time.time()
            internet_latency = round((end_time - start_time) * 1000)
            await ctx.send(f'Bot Latency: {latency}ms\nInternet Latency: {internet_latency}ms')
        except requests.ConnectionError:
            await ctx.send('No internet connection.')

    @client.command(name='play', help='Plays music in a voice channel')
    async def play(ctx, url):
        channel = ctx.author.voice.channel
        voice_channel = get(client.voice_clients, guild=ctx.guild)

        with youtube_dl.YoutubeDL({}) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']

        voice_channel.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))

    @client.command(name='stop', help='Stops playing music and disconnects the bot')
    async def stop(ctx):
        voice_channel = get(client.voice_clients, guild=ctx.guild)
        if voice_channel.is_playing():
            voice_channel.stop()
        await voice_channel.disconnect()
    # ================================== Channel Management =============================================
    @client.command(name='create_channel')
    async def create_channel(ctx, channel_name: str, channel_type: str = 'text'):
        guild = ctx.guild

        if channel_type.lower() == 'text':
            existing_channel = discord.utils.get(guild.channels, name=channel_name)

            if not existing_channel:
                await guild.create_text_channel(channel_name)
                await ctx.send(f'Text channel `{channel_name}` created successfully!')
            else:
                await ctx.send(f'Text channel `{channel_name}` already exists.')
        elif channel_type.lower() == 'voice':
            existing_channel = discord.utils.get(guild.channels, name=channel_name)

            if not existing_channel:
                await guild.create_voice_channel(channel_name)
                await ctx.send(f'Voice channel `{channel_name}` created successfully!')
            else:
                await ctx.send(f'Voice channel `{channel_name}` already exists.')
        else:
            await ctx.send('Invalid channel type. Use "text" or "voice".')

    @client.command(name='edit_channel')
    async def edit_channel(ctx, channel_name: str, new_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel:
            await channel.edit(name=new_name)
            await ctx.send(f'Channel `{channel_name}` edited successfully!')
        else:
            await ctx.send(f'Channel `{channel_name}` not found.')

    @client.command(name='delete_channel')
    async def delete_channel(ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel:
            await channel.delete()
            await ctx.send(f'Channel `{channel_name}` deleted successfully!')
        else:
            await ctx.send(f'Channel `{channel_name}` not found.')

    @client.command(name='create_voice_channel')
    async def create_voice_channel(ctx, channel_name: str):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)

        if not existing_channel:
            await guild.create_voice_channel(channel_name)
            await ctx.send(f'Voice channel `{channel_name}` created successfully!')
        else:
            await ctx.send(f'Voice channel `{channel_name}` already exists.')

    @client.command(name='edit_voice_channel')
    async def edit_voice_channel(ctx, channel_name: str, new_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel and isinstance(channel, discord.VoiceChannel):
            await channel.edit(name=new_name)
            await ctx.send(f'Voice channel `{channel_name}` edited successfully!')
        else:
            await ctx.send(f'Voice channel `{channel_name}` not found.')

    @client.command(name='delete_voice_channel')
    async def delete_voice_channel(ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel and isinstance(channel, discord.VoiceChannel):
            await channel.delete()
            await ctx.send(f'Voice channel `{channel_name}` deleted successfully!')
        else:
            await ctx.send(f'Voice channel `{channel_name}` not found.')

    # ================================== stopwatch Management =============================================
    @client.command(name='create_stopwatch')
    async def create_stopwatch(ctx, duration: str):
        stopwatch_channel = get_or_create_channel(ctx.guild, stopwatch_channel_name)
        await create_and_start_stopwatch(ctx.author, duration, stopwatch_channel)

    @client.command(name='create_reminder')
    async def create_reminder(ctx, duration: str, *, description: str):
        reminder_channel = get_or_create_channel(ctx.guild, reminder_channel_name)
        await create_and_start_reminder(ctx.author, duration, description, reminder_channel)

    async def get_or_create_channel(guild, channel_name):
        channel = discord.utils.get(guild.channels, name=channel_name)
        if not channel:
            channel = await guild.create_text_channel(channel_name)
        return channel

    def parse_duration(duration):
        matches = re.findall(r'(\d+)([hms])', duration)
        total_seconds = 0
        for time_value, unit in matches:
            time_value = int(time_value)
            if unit == 'h':
                total_seconds += time_value * 3600
            elif unit == 'm':
                total_seconds += time_value * 60
            elif unit == 's':
                total_seconds += time_value
        return total_seconds

    async def create_and_start_stopwatch(author, duration, channel):
        duration_seconds = parse_duration(duration)
        await channel.send(f'Stopwatch created for {duration}.')
        client.loop.create_task(stopwatch_task(author, duration_seconds, channel))

    async def create_and_start_reminder(author, duration, description, channel):
        duration_seconds = parse_duration(duration)
        await channel.send(f'Reminder set for {duration}: {description}')
        client.loop.create_task(reminder_task(author, duration_seconds, description, channel))

    async def stopwatch_task(author, duration_seconds, channel):
        await asyncio.sleep(duration_seconds)
        await channel.send(
            f'{author.mention}, your stopwatch for {duration_seconds // 3600} hours, {duration_seconds % 3600 // 60} minutes, and {duration_seconds % 60} seconds is complete!')

    async def reminder_task(author, duration_seconds, description, channel):
        await asyncio.sleep(duration_seconds)
        await channel.send(f'{author.mention}, reminder: {description}')


    client.run(values.Token)
