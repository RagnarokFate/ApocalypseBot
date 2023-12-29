import random
import time

async def sent_message(message,user_message,is_private):
    status = ""
    if(is_private):
        status = "Direct Message"
    else:
        status = "Server Message"
    try:
        response = main_message_handler(user_message,status)
        if is_private:  # response via Direct Message
            await message.author.send(response)
        else:           # response via Server Message
            await message.channel.send(response)
    except Exception as e:
        print(e)

def main_message_handler(message,status)->str:
    message_lowercase = message.lower()
    if status == "Direct Message":
        response = message_handler_DirectMessage(message_lowercase)
    elif status == "Server Message":
        response = message_handler_ServerMessage(message_lowercase)
    return response


def message_handler_DirectMessage(message_lowercase) -> str:
    # ! - Commands
    print("Response To Direct Message\n")
    if message_lowercase.startswith('hello admin'):
        return 'Admin says hi :D!'
    elif message_lowercase == 'test':
        # TODO - CREATE PING PONG INTERNET TEST
        return 'This is a test!'
    elif message_lowercase.startswith('roll'):
        return str(random.randint(1, 6))
    # The Two below commands belong also to Non-user
    elif message_lowercase == 'help':
        return "'This is a help message, what i can do for you?'"
    elif message_lowercase == 'commands':
        return "'This is a command list message ... '" # TODO
    elif message_lowercase == 'contact':
        return "'these are the social media account : RagnarokFate will reach back to you as soon as possible '" # TODO


def message_handler_ServerMessage(message_lowercase) -> str:
    # / - Commands
    print("Response To Server Message\n")
    # Let's divide into categories :
    # ======================================================================================================
    # Main Responses for bot
    if message_lowercase == 'test':
        # TODO - CREATE PING PONG INTERNET TEST
        return 'This is a test!'
    elif message_lowercase.startswith('roll'):
        return str(random.randint(1, 6))
    # The Two below commands belong also to Non-user
    elif message_lowercase == 'help':
        return "'This is a help message, what i can do for you?'"
    elif message_lowercase == 'commands':
        return "**Channel Commands (Voice Or Text)** \n/CreateC - Creates a channel in the server \n/DeleteC - Deletes a channel in the server \n/RenameC - Renames a channel in the server \n/SetCDC - setup a cooldown on a channel \n**Exam Commands** \n/Create_Timestop - Creates a Timerstop \n/Pause_Timestop - pauses the current Timerstop \n/Stop_Timestop - removes the current Timerstop \n/Reset_Timestop - resets the timer to previous input \n/ReminderTimeStop (screen or voice) - creates a reminder for the timerstop \n/ScreenPreview - provide survilience over Screenshare or Video Call \n/SetEvent - setting up an event \n/CancelEvent - cancel up an event \n**Student Commands** \n/SendTo On - sending texts/files to specfic channel nonstop untill /SendTo OFF command has been acquired \n /SendTo OFF - stops sending to specific channel \n/PlayMusic - plays an audio at user's current voice chat \n/PauseMusic - pauses the audio that is being played at user's current voice chat \n/StopMusic - stops the bot from playing audio at voice chat (reset the music queue) \n/MusicQueue - displays the music queue \n/MusicRemove - removes a specfic music via index or name \n/Upload file - uploading a file to a personal online cloud \n/Cal - calculating a given equation \n/BingChat - uses BingChat service \n/BingImage - uses BingImage service \n**Users Commands** \n/SendMessage (Private or public) - sends message to role or user. \n/Roll - rolls a number between 1 to 6. \n/Notify - get notification on something (no idea yet) \n/Socials - provides the socials of bot's Admin - RagnarokFate. \n "

    # ======================================================================================================
    # VOICE CHAT INTERACTION
    elif message_lowercase == 'join':
        return "'The bot has joined the voice chat!'"  # TODO
    elif message_lowercase == 'disconnect':
        return "'The bot has left the voice chat!'"  # TODO

    # ======================================================================================================
