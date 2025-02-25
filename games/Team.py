"""
    Clase Team:

"""
from Athlete import Athlete as athlete
from Sport import Sport as sport

class Team:
    def __init__(self, name:str, sport:sport, players:list):
        self.name = name 
        self.sport = sport
        self.players= players
        
    def __str__(self):
        return f"Team:{self.name}, {self.sport}, {self.players}"
    
    def __repr__(self):
        return f"Team(name='{self.name}', sport={self.sport}, players= {self.players})"
    
    def to_json(self)->dict:
        return {"name":self.name, "sport": self.sport.to_json(), "players": [p.to_json for p in self.players]}
    
    
if __name__ == '__main__':
    a1 = athlete("Michael Jordan")
    a2 = athlete("Kobe Bryant")
    a3 = athlete("Lebron James")
    a4 = athlete("Jordan Pole")
    a5 = athlete("Stephen Curry")
    a6 = athlete("Tim Duncan")
    
    players = [a1,a2,a3,a4,a5,a6]
    
    s = sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers",s,players=players)
    print(lakers)
    