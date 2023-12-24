import random

class CreatureCard:
    def __init__(self, name, attacks, type):
        self.name = name
        self.attacks = attacks  # Here is the list of tuples (attack name, attack power)
        self.type = type

    def __str__(self):
        attacks_str = ', '.join([f"{name} ({power} dmg)" for name, power in self.attacks])
        return f"{self.name} (Attacks: {attacks_str}, Type: {self.type})"

class EnhancementCard:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __str__(self):
        return f"{self.name} (Effect: {self.effect})"

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.active_enhancements = []

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            print(f"{self.name} drew {card}")

    def play_creature(self):
        creature_cards = [card for card in self.hand if isinstance(card, CreatureCard)]
        if creature_cards:
            return creature_cards.pop(0)
        return None

    def play_enhancement(self):
        enhancement_cards = [card for card in self.hand if isinstance(card, EnhancementCard)]
        if enhancement_cards:
            enhancement = enhancement_cards.pop(0)
            self.active_enhancements.append(enhancement)
            print(f"{self.name} played {enhancement}")
            return enhancement
        return None

def create_deck():
    creatures = [
        CreatureCard("Phoenix", [("Flame Wing", 7), ("Fire Blast", 5)], "Fire"),
        CreatureCard("Leviathan", [("Tidal Wave", 8), ("Aqua Slam", 6)], "Water"),
        CreatureCard("Dracula", [("Vampiric Bite", 7), ("Shadow Strike", 6)], "Dark"),
        CreatureCard("Goliath", [("Stone Throw", 6), ("Earthquake", 7)], "Earth"),
        CreatureCard("Kraken", [("Whirlpool", 8), ("Tentacle Crush", 7)], "Water"),
        CreatureCard("Dragon", [("Fire Breath", 9), ("Tail Swipe", 6)], "Fire"),
        CreatureCard("Unicorn", [("Horn Charge", 6), ("Healing Light", 4)], "Light"),
        CreatureCard("Wizard", [("Magic Missile", 5), ("Arcane Blast", 4)], "Arcane"),
        CreatureCard("Werewolf", [("Lunar Strike", 7), ("Feral Claw", 6)], "Dark"),
    ]
    enhancements = [
        EnhancementCard("Mystic Forest", "+2 Defense to all creatures"),
        EnhancementCard("Volcanic Terrain", "+3 Attack to Fire creatures"),
    ]
    deck = creatures * 4 + enhancements * 2
    random.shuffle(deck)
    return deck

def battle(player1, player2):
    creature1 = player1.play_creature()
    creature2 = player2.play_creature()

    if creature1 and creature2:
        print(f"{player1.name}'s {creature1.name} battles {player2.name}'s {creature2.name}!")
        #  attack choice & battle logic here
        print("Battle phase...")

# Game Setup (up to 4 players)
player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
players = [Player(name) for name in player_names]
for player in players:
    player.deck = create_deck()

# Game Loop (one round)
for _ in range(5):
    for player in players:
        player.draw_card()

# Battle phase for each pair of players
for i in range(len(players) - 1):
    for j in range(i + 1, len(players)):
        battle(players[i], players[j])
