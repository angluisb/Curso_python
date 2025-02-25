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
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl = Sport("Fotball", 11, "NFL")
    lmp = Sport("Baseball",9, "LMP")
    mlb = Sport("Baseball",9, "MLB")
    
    lista_deportes = [nfl,lmp,mlb]
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes,"w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")
        sport_list=[]
        with open(archivo_deportes,"r") as file:
            for line in file:
                d = eval(line)
                sport_list.append(d)
        print(sport_list)
        
    import json
    archivo_json = "deportes.json"
    sports_json = [sport.to_json() for sport in sport_list]
    with open(archivo_json,"w")as file:
        json.dump(sports_json,file, indent=4)
        
    sport_list_json = []
    with open(archivo_json, "r")as file:
        sport_list_json = json.load(file)
    print(sport_list_json)
