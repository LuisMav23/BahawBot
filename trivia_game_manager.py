import requests


class TriviaGameManager:
    categories = {}
    chosen_category = ''
    isGameInProgress = False
    
    def __init__(self):
        self.categories = self.get_categories()
        isGameInProgress = True
        
    
    async def begin(self):
        pass
    
    async def stop(self):
        pass
    
    async def restart(self):
        pass
    
    def get_categories(self):
        return requests.get('https://opentdb.com/api_category.php').json
    
    def get_questions(self):
        pass