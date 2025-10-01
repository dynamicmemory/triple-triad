from triple_triad.card import Card 

class Player:

    def __init__(self, name):
        self.name = name
        self.score: int = 5
        self.hand: dict = self.deal_hand() 


    def deal_hand(self) -> dict:
        """
        Generate a hand of 5 cards for a player 
        """
        hand = {}
        for num in range(5):
            hand[f"card_{num}"] = Card(self.name, num).generate_card()
        return hand


    def get_unplayed_cards(self) -> list:
        """
        Returns a list of cards a player has not played yet.
        """
        cards = []
        for card in self.hand:
            if not self.hand[card]["played"]:
                cards.append(self.hand[card])
        return cards


    def set_played_card(self, card: str) -> None:
        """ 
        Sets a cards "played" variable to true
        """
        self.hand[card]["played"] = True


    def get_card(self, card: str) -> Card:
        return self.hand[card]


    def update_score(self):
        pass


