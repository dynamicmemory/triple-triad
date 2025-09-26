class Board:

    def __init__(self):
        self.gameover: bool = False
        self.empty_squares: int = 9


    def is_gameover(self):
        if self.empty_squares == 0:
            self.gameover = True 


