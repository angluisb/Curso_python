class Sport:
    def __init__(self, name:str, players:int, league:str):
        self.name = name
        self.players = int(players)
        self.league = league
        
    def __str__(self):
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self):
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self) -> dict:
        """Convertir a JSON"""
        return {"name":self.name, "players":self.players, "league":self.league}
    
    
if __name__ == "__main__":
    nfl = Sport("Fotball", 11, "NFL")
    print(nfl)
    print(repr(nfl))
    print(nfl.to_json)