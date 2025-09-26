class Card:

    def __init__(self, top, right, left, bottom, owner, played):
        self.top: int = top
        self.right: int = right 
        self.left: int = left
        self.bot: int = bottom
        self.owner: str = owner
        self.played: bool = played

    
    def is_played(self):
        pass         


