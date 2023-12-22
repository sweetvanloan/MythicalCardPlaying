import random

class CreatureCard:
    def __init__(self, name, attack, defense, type):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.type = type

    def __str__(self):
        return f"{self.name} (Attack: {self.attack}, Defense: {self.defense}, Type: {self.type})"

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []

    def draw_card(self):
        if self.deck:
            card = self.deck.pop()
            self.hand.append(card)
            print(f"{self.name} drew {card}")
        else:
            print(f"{self.name}'s deck is empty!")

    def play_card(self):
        if self.hand:
            return self.hand.pop(random.randint(0, len(self.hand) - 1))
        else:
            print(f"{self.name} has no cards to play!")
            return None

def create_deck():
    creatures = [
        CreatureCard("Phoenix", 5, 4, "Fire"),
        CreatureCard("Leviathan", 8, 7, "Water"),
        CreatureCard("Dracula", 6, 5, "Dark"),
        CreatureCard("Goliath", 7, 6, "Earth"),
        # Add more creatures here
    ]
    deck = creatures * 5  # Repeat creatures to fill the deck
    random.shuffle(deck)
    return deck

def battle(card1, card2):
    print(f"{card1.name} battles {card2.name}!")
    if card1.attack > card2.defense:
        print(f"{card1.name} wins!")
    elif card1.attack < card2.defense:
        print(f"{card2.name} wins!")
    else:
        print("The battle is a draw!")

# Game Setup
player1 = Player("Player 1")
player2 = Player("Player 2")
player1.deck = create_deck()
player2.deck = create_deck()

# Game Loop (for one round)
for _ in range(5):
    player1.draw_card()
    player2.draw_card()

card1 = player1.play_card()
card2 = player2.play_card()

if card1 and card2:
    battle(card1, card2)
