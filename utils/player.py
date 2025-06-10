import random
from utils.card import Card 

class Player(self):
    def __init__(self):
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

def add_card(self,card: Card):
    self.cards.append(card)
    self.number_of_cards = len(self.cards)

def play(self):
    if not self.cards:
        print(f"{self.name} n'a plus de carte à jouer.")
        return None
    
    card = random.choice(self.cards)
    self.cards.remove(card)
    self.history.append(card)
    self.turn_count += 1
    self.number_of_card = len(self.cards)

    print(f"{self.name} {self.turn_count} played : {card.value} {card.icon}")
    return card

class Deck:
    def __initi__(self):
        self.cards = []

    def fill_deck(self):
        """Remplit le deck avec 52 cartes : 13 valeurs × 4 symboles."""
        symbols = [
            ("rouge", "♥"),
            ("rouge", "♦"),
            ("noir", "♣"),
            ("noir", "♠")
        ]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.cards = []  

        for color, icon in symbols:
            for value in values:
                self.cards.append(Card(color, icon, value))

    def shuffle(self):
        """Mélange les cartes du deck."""
        random.shuffle(self.cards)

    def distribute(self, players: list[Player]):
        """Distribue les cartes équitablement entre tous les joueurs."""
        if not players:
            print("Aucun joueur à qui distribuer les cartes.")
            return

        player_index = 0
        while self.cards:
            player = players[player_index]
            card = self.cards.pop(0)
            player.add_card(card)
            player_index = (player_index + 1) % len(players)