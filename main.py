import asyncio

import discord
from discord.ext import commands
import responses
import values
import os

stopwatch_channel_name = "stopwatch"
reminder_channel_name = "reminders"

intents = discord.Intents.default()  # Create a default set of intents
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='/',intents=intents)

Services_list = []


def run_discord_bot():
    load_extensions()

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


    client.run(values.Token)

def load_extensions():
    # Loading Services into project
    for filename in os.listdir('./Services'):
        if filename.endswith('.py'):
            Services_list.append(filename[:-3])
    print(Services_list)

    for Service in Services_list:
        client.load_extension(Service)

    return


if __name__ == '__main__':
    run_discord_bot()

