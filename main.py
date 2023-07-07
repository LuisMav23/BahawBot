import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from game_manager import GameInfoManager


# loads the .env file where the TOKEN is stored
load_dotenv()

# initialize intents and bot
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True
game_manager = None
bot = commands.Bot(command_prefix='$' ,intents=intents)


# gets called when bot runs
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# a command that begins the game
@bot.command()
async def begin(ctx, game):
    global game_manager
    game_manager = GameInfoManager(game, ctx)
    await game_manager.manager.begin()
    

@bot.command()
async def guess(ctx, guess):
    global game_manager
    if game_manager.get_active() != 'WORDLE':
        await ctx.send('Wordle game is currently inactive')
        return
    
    await game_manager.manager.guess(guess)
    # if guessPattern == ':green_square: :green_square: :green_square: :green_square: :green_square: ':
    #     await ctx.send('You won!')
    #     isGameInProgress = False
    #     tries = 5
    #     wordGuesses = []
    #     wordleWord = ''
    #     return

@bot.command()
async def send(ctx):
    await ctx.send("hello\nhello")


if __name__ == '__main__':
        bot.run(os.getenv('TOKEN'))
