import random as r

class Card:

    def __init__(self, owner):
        self.owner: str = owner
        self.played: bool = False 

    
    # TODO: Hardcoding card values, needs scaleable system
    def generate_card(self):
        values = {}
        directions = ["north", "east", "south", "west"]
        for dir in directions:
            values[dir] = r.randint(1, 5)
        values["player"] = self.owner 
        values["played"] = self.played
        return values


    def is_played(self):

        pass         

    

