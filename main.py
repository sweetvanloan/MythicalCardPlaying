import random

class CreatureCard:
    def __init__(self, name, attack, defense, type):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.type = type

    def __str__(self):
        return f"{self.name} (A: {self.attack}, D: {self.defense}, Type: {self.type})"

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop(0))
            print(f"{self.name} drew {self.hand[-1]}")

    def play_card(self):
        return self.hand.pop(0) if self.hand else None

def create_deck():
    creatures = [
        CreatureCard("Phoenix", 5, 4, "Fire"),
        CreatureCard("Leviathan", 8, 7, "Water"),
        CreatureCard("Dracula", 6, 5, "Dark"),
        CreatureCard("Goliath", 7, 6, "Earth"),
        CreatureCard("Kraken", 7, 6, "Water"),
        CreatureCard("Dragon", 9, 7, "Fire"),
        CreatureCard("Unicorn", 6, 5, "Light"),
        CreatureCard("Wizard", 5, 4, "Arcane"),
        CreatureCard("Werewolf", 7, 6, "Dark")
    ]
    deck = creatures * 5
    random.shuffle(deck)
    return deck

def battle(card1, card2):
    if card1 and card2:
        print(f"{card1.name} battles {card2.name}!")
        if card1.attack > card2.defense:
            print(f"{card1.name} wins!")
        elif card1.attack < card2.defense:
            print(f"{card2.name} wins!")
        else:
            print("The battle is a draw!")

# Game Setup
player1, player2 = Player("Player 1"), Player("Player 2")
player1.deck, player2.deck = create_deck(), create_deck()

# Game Loop (one round)
for _ in range(5):
    player1.draw_card()
    player2.draw_card()

battle(player1.play_card(), player2.play_card())
