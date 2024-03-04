import discord
from discord.ext import commands

class TimeStop(commands.Cog):
    def __int__(self,client):
        self.client = client

    # create a set of functions that will provide the necessary operations.



def setup(client):
    client.add_cog(TimeStop(client))

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