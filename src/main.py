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
    print(f'Logged in as {bot.user}')

# a command that begins the game
@bot.command()
async def begin(ctx, game):
    global game_manager
    game_manager = GameInfoManager(game, ctx)
    if game_manager.get_active() == 'NONE':
        await ctx.send('Invalid game')
        del game_manager
        game_manager = None
        return
    await game_manager.manager.begin()
    

@bot.command()
async def guess(ctx, guess):
    global game_manager
    if game_manager == None:
        await ctx.send(':bangbang:**No game is currently active**:bangbang:')
        return
    
    if game_manager.get_active() != 'WORDLE':
        await ctx.send(':bangbang:**Another game is currently active**:bangbang:')
        return
    
    await game_manager.manager.guess(guess)
    if not game_manager.manager.isGameInProgress:
        del game_manager
    
@bot.command()
async def stop(ctx):
    global game_manager
    if game_manager == None:
        await ctx.send(':bangbang:**No game is currently active**:bangbang:')
        return
    del game_manager
    game_manager = None
    await ctx.send("Game Stopped")

@bot.command()
async def restart(ctx):
    global game_manager
    if game_manager == None:
        await ctx.send(':bangbang:**No game is currently active**:bangbang:')
        return
    await game_manager.manager.restart()

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
