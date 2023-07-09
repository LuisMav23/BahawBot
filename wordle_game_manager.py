import requests
import nltk
from nltk.corpus import words

''' WORDLE GAME MANAGER '''

class WordleGameManager:
    ctx = None
    Word = ''
    Guesses = []
    is_game_in_progerss = False
    
    
    def __init__(self, ctx):
        nltk.download('words')
        self.ctx = ctx
        self.Word = self.get_wordle_word()
        while not self.is_valid_word(self.Word):
            self.Word = self.get_wordle_word()
        self.Guesses = []
        self.is_game_in_progerss = True
    
    # sends a message that the game has started
    async def begin(self):
        message = ':green_square: :yellow_square: :regional_indicator_w: :regional_indicator_o: :regional_indicator_r: :regional_indicator_d: :regional_indicator_l: :regional_indicator_e: :yellow_square: :green_square:\n'
        message += "**Welcome to wordle, here are the instructions:**\n"
        message += '- To guess type **$guess <Your Guess>**.\n- Stop the game type **$stop** (to restart type **$restart**).\n' #\n- You have 5 Tries.\n- Only guess 5 letter words (musct be a valid word).    
        message += '- **BLOCKS:**\n> :blue_square:  Letter is not in the word\n> :yellow_square:  Letter is not in the right place\n> :green_square:  Letter is in the right place'
        await self.ctx.send(message)
        
    
    async def guess(self, guess):
        if len(guess) != 5:
            await self.ctx.send('only enter a 5 letter word')
            return
        
        if not self.is_valid_word(guess):
            await self.ctx.send('only enter a valid english word')
            return
            
        guessPattern = ''
        guess = guess.upper()
        # :yellow_square: :blue_square: :green_square:
        for i in range(len(self.Word)):
            if guess[i] == self.Word[i]:
                guessPattern += ':green_square: '
            elif guess[i] in self.Word:
                guessPattern += ':yellow_square: '
            else:
                guessPattern += ':blue_square: '
        self.Guesses.append({
                "word": guess,
                "pattern": guessPattern
            })
        message = ''
        for guess_dict in self.Guesses:
            word_temp = guess_dict['word']
            pattern_temp = guess_dict['pattern']
            message += f'{pattern_temp}\t-\t**{word_temp}**\n'
            
        if guessPattern == ':green_square: :green_square: :green_square: :green_square: :green_square: ':
            message += '**CONRATULATIONS YOU GUESSED THE WORD**'
            self.is_game_in_progerss = False
        
        if len(self.Guesses) == 6:
            message += f'**You Lost, the word was {self.Word}**'
            self.is_game_in_progerss = False
            
        await self.ctx.send(message)
    
    async def stop(self):
        self.ctx = None
        self.Word = ''
        self.Guesses = []
        self.is_game_in_progerss = False
    
    async def restart(self):
        self.Word = self.get_wordle_word()
        self.Guesses = []
        self.is_game_in_progerss = True
        self.ctx.send("restarting game...")
        await self.begin()
    
    def get_wordle_word(self):
        url = 'https://random-word-api.vercel.app/api?words=1&length=5&type=uppercase'
        response = requests.get(url)
        word = response.json()[0]
        return word

    def is_valid_word(self, word):
        return word.lower() in words.words()