import random as r

class Card:

    def __init__(self, owner, number):
        self.owner: str = owner
        self.played: bool = False 
        self.number: int = number

    
    # TODO: Hardcoding card values, needs scaleable system
    def generate_card(self):
        values = {}
        directions = ["north", "east", "south", "west"]
        for dir in directions:
            values[dir] = r.randint(1, 5)
        values["player"] = self.owner 
        values["played"] = self.played
        values["name"] = f"card_{self.number}"
        return values


    # def update_owner(self, player: str):
    #     self.owner = player

    def is_played(self):

        pass         

    

