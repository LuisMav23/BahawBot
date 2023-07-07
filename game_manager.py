import requests

# gets a random word from random-word-api


class GameInfoManager:
    active_game = 'NONE'
    manager = None
    
    
    def __init__(self, active_game, ctx):
        self.active_game = active_game
        
        if self.active_game == 'WORDLE':
            self.manager = WordleGameManager(ctx)
        
    def get_active(self):
        return self.active_game
        
class WordleGameManager:
    ctx = None
    Word = ''
    Guesses = []
    
    def __init__(self, ctx):
        self.ctx = ctx
        self.Word = self.get_wordle_word()
        self.Guesses = []
    
    # sends a message that the game has started
    async def begin(self):
        message = ":green_square: :yellow_square: :regional_indicator_w: :regional_indicator_o: :regional_indicator_r: :regional_indicator_d: :regional_indicator_l: :regional_indicator_e: :yellow_square: :green_square:\n"
        message += "**Welcome to wordle, here are the instructions:**\n"
        message += "- To guess type **$guess <Your Guess>**.\n- Stop the game type **$stop** (to restart type **$restart**).\n" #\n- You have 5 Tries.\n- Only guess 5 letter words (musct be a valid word).    
        message += "- BLOCKS:\n\t- :blue_square: : Letter is not in the word\t :yellow_square: : Letter is not in the right place\t :green_square: : Letter is in the right place"
        await self.ctx.send(message)
        
    async def guess(self, guess):
        if len(guess) != 5:
            await self.ctx.send('')
            return
        guessPattern = ''
        guess = guess.upper()
        print(type(self.Word))
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
            message += f'{word_temp}\t-\t{pattern_temp}\n'
        await self.ctx.send(message)
        
    
    def get_wordle_word(self):
        url = "https://random-word-api.vercel.app/api?words=1&length=5&type=uppercase"
        response = requests.get(url)
        word = response.json()[0]
        return word