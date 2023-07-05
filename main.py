import os
from dotenv import load_dotenv
import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True
intents.voice_states = True
client = discord.Client(intents=intents)

queue = []
is_playing = False

def check_queue():
    global is_playing, queue
    
    if len(queue) > 0:
        is_playing = True
        url = queue[0]['url']
        
    


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$play'):
        if not message.author.voice:
            await message.channel.send("You must be in a voice channel to use this command.")
            return
        voice_channel = message.author.voice.channel
        if not voice_channel:
            await message.channel.send("You must be in a voice channel to use this command.")
            return

     

    



client.run(os.getenv('TOKEN'))