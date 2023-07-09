import requests

from wordle_game_manager import WordleGameManager

# GAME MANAGER INTERFACE
#   - BEGIN DEF
#   - STOP DEF
#   - RESTART DEF


class GameInfoManager:
    active_game = 'NONE'
    manager = None
    
    
    def __init__(self, active_game, ctx):
        self.active_game = active_game.upper()
        
        if self.active_game == 'WORDLE':
            self.manager = WordleGameManager(ctx)
        else:
            self.active_game = 'NONE'
        
    def get_active(self):
        return self.active_game
    
    def __del__(self):
        self.active_game = 'NONE'
        if self.manager:
            del self.manager



    


    
    