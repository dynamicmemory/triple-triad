from __future__ import annotations
from typing import TYPE_CHECKING
from triple_triad.card import Card 
from triple_triad.randomAgent import RandomAgent
from triple_triad.humanAgent import HumanAgent

if TYPE_CHECKING:
    from humanAgent import HumanAgent
    from randomAgent import RandomAgent 

class Player:

    def __init__(self, name, agent, ai):
        self.name = name
        self.score: int = 5
        self.hand: dict = self.deal_hand() 
        self.agent: HumanAgent|RandomAgent|None = agent
        self.ai: bool|None = ai 
        

    def set_agent(self, agent_type: str) -> None:
        """
        Sets the type of agent the player is and whether they are AI or human
        Params: str - human, ai, (eventually - random, minimax, etc)
        """
        # Add fields for type of agent depending on difficulty
        if agent_type == "human":
            self.agent = HumanAgent()
            self.ai = False 
        elif agent_type == "ai":
            self.agent = RandomAgent()
            self.ai = True 


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
        """ 
        Returns a card object from a giving name 
        """
        return self.hand[card]


    def get_agent(self) -> None|HumanAgent|RandomAgent:
        """ 
        Returns the agent controlling a player 
        """
        return self.agent
