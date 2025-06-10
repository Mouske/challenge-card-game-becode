import random
from utils.card import Card
from utils.player import Player

class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        self.cards = []
        symbols = [
            ("rouge", "♥"),
            ("rouge", "♦"),
            ("noir", "♣"),
            ("noir", "♠")
        ]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for color, icon in symbols:
            for value in values:
                self.cards.append(Card(color, icon, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, players: list[Player]):
        if not players:
            print("Aucun joueur.")
            return
        while self.cards:
            for player in players:
                if self.cards:
                    player.add_card(self.cards.pop(0))


class Board:
    def __init__(self, players: list[Player]):
        self.players = players              
        self.turn_count = 0                 
        self.active_cards = {}              
        self.history_cards = []            

    def start_game(self):
        print("Début de la partie.")
        # 1. Créer et préparer le deck
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        # 2. Distribuer les cartes aux joueurs
        deck.distribute(self.players)

        # 3. Boucle de jeu : chaque joueur joue 1 carte par tour tant qu'il a des cartes
        while any(player.number_of_cards > 0 for player in self.players):
            self.turn_count += 1
            self.active_cards.clear()

            for player in self.players:
                card_played = player.play()
                if card_played:
                    self.active_cards[player.name] = card_played

            # Ajouter toutes les cartes jouées ce tour dans l'historique
            self.history_cards.extend(self.active_cards.values())

            # Affichage de fin de tour
            print(f"\nTour {self.turn_count} terminé.")
            print("Cartes actives ce tour :")
            for pname, card in self.active_cards.items():
                print(f" - {pname} a joué {card.value} {card.icon}")
            print(f"Nombre total de cartes jouées (hors actives) : {len(self.history_cards)}\n")
