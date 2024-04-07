import discord
from discord.ext import commands


class ChannelMangement(commands.Cog):
    def __int__(self, client):
        self.client = client

    # ================================== Channel Management =============================================
    @commands.command(name='create_channel')
    async def create_channel(self,ctx, channel_name: str, channel_type: str = 'text'):
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

    @commands.command(name='edit_channel')
    async def edit_channel(self,ctx, channel_name: str, new_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel:
            await channel.edit(name=new_name)
            await ctx.send(f'Channel `{channel_name}` edited successfully!')
        else:
            await ctx.send(f'Channel `{channel_name}` not found.')

    @commands.command(name='delete_channel')
    async def delete_channel(self,ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel:
            await channel.delete()
            await ctx.send(f'Channel `{channel_name}` deleted successfully!')
        else:
            await ctx.send(f'Channel `{channel_name}` not found.')

    @commands.command(name='create_voice_channel')
    async def create_voice_channel(self,ctx, channel_name: str):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)

        if not existing_channel:
            await guild.create_voice_channel(channel_name)
            await ctx.send(f'Voice channel `{channel_name}` created successfully!')
        else:
            await ctx.send(f'Voice channel `{channel_name}` already exists.')

    @commands.command(name='edit_voice_channel')
    async def edit_voice_channel(self,ctx, channel_name: str, new_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel and isinstance(channel, discord.VoiceChannel):
            await channel.edit(name=new_name)
            await ctx.send(f'Voice channel `{channel_name}` edited successfully!')
        else:
            await ctx.send(f'Voice channel `{channel_name}` not found.')

    @commands.command(name='delete_voice_channel')
    async def delete_voice_channel(self,ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel and isinstance(channel, discord.VoiceChannel):
            await channel.delete()
            await ctx.send(f'Voice channel `{channel_name}` deleted successfully!')
        else:
            await ctx.send(f'Voice channel `{channel_name}` not found.')

def setup(client):
    client.add_cog(ChannelMangement(client))