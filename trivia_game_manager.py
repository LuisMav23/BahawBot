import requests


class TriviaGameManager:
    questions_info = {}
    is_game_in_progress = False
    ctx = None
    
    def __init__(self, ctx):
        self.categories = self.get_categories()
        self.is_game_in_progress = True
        self.ctx = ctx
        
    
    async def begin(self):
        pass
    
    async def stop(self):
        pass
    
    async def restart(self):
        pass
    
    def get_categories(self):
        return requests.get('https://opentdb.com/api_category.php').json
    
    def get_questions(self):
        response = requests.get('https://opentdb.com/api.php?amount=5&type=multiple').json
        questions = response['resuslts']
        info = {
            
        }