import message_handler
import values
import os
import nextcord
from nextcord.ext import commands


Services_list = []
client = None

def load_extensions():
    # Loading cogs into project
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            Services_list.append(filename[:-3])
            client.load_extension('ApocalypseBot.cogs.' + filename)

    print(Services_list)
    pass

def run_discord_bot():
    load_extensions()


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        message_handler(message,client)

    # Bot event, just like before
    @client.event
    async def on_member_join(member):
        embed = nextcord.Embed(title=f"Welcome to {member.guild.name}!",
                              description=f"Welcome {member.mention} to our server!", colour=0x46b8a3)
        embed.set_author(name="Apocalypse Bot",icon_url="ApocalypseBot/images/bot_pfp.jpeg")
        embed.set_thumbnail(url="ApocalypseBot/images/banner_image.jpeg")
        # embed.add_field(name="",value="",inline=True)
        # embed.add_field(name="",value="",inline=True)
        # embed.add_field(name="",value="",inline=True)
        embed.set_footer(text="Thanks for joining in!")
        await member.send(embed=embed)

    client.run(values.Token)




if __name__ == '__main__':
    intents = nextcord.Intents.default()
    intents.message_content = True
    intents.members = True

    client = commands.Bot(command_prefix='!', intents=intents)


    run_discord_bot()


