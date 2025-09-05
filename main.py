import random

class CreatureCard:
    def __init__(self, name, attacks, type):
        self.name = name
        self.attacks = attacks  # List of tuples (attack name, attack power)
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
        for i, card in enumerate(self.hand):
            if isinstance(card, CreatureCard):
                return self.hand.pop(i)  # remove from hand correctly
        print(f"{self.name} has no creature to play!")
        return None

    def play_enhancement(self):
        for i, card in enumerate(self.hand):
            if isinstance(card, EnhancementCard):
                enhancement = self.hand.pop(i)  # remove from hand correctly
                self.active_enhancements.append(enhancement)
                print(f"{self.name} played {enhancement}")
                return enhancement
        return None

def create_deck():
    creatures = [
        CreatureCard("Phoenix",   [("Flame Wing", 7), ("Fire Blast", 5)], "Fire"),
        CreatureCard("Leviathan", [("Tidal Wave", 8), ("Aqua Slam", 6)], "Water"),
        CreatureCard("Dracula",   [("Vampiric Bite", 7), ("Shadow Strike", 6)], "Dark"),
        CreatureCard("Goliath",   [("Stone Throw", 6), ("Earthquake", 7)], "Earth"),
        CreatureCard("Kraken",    [("Whirlpool", 8), ("Tentacle Crush", 7)], "Water"),
        CreatureCard("Dragon",    [("Fire Breath", 9), ("Tail Swipe", 6)], "Fire"),
        CreatureCard("Unicorn",   [("Horn Charge", 6), ("Healing Light", 4)], "Light"),
        CreatureCard("Wizard",    [("Magic Missile", 5), ("Arcane Blast", 4)], "Arcane"),
        CreatureCard("Werewolf",  [("Lunar Strike", 7), ("Feral Claw", 6)], "Dark"),
        CreatureCard("Poltergeist",[("Eerie Wail", 6), ("Haunting Presence", 5)], "Spirit"),
        CreatureCard("Kitsune",   [("Foxfire", 7), ("Illusion", 5)], "Mystic"),
        CreatureCard("Kraken",    [("Tsunami", 8), ("Ink Cloud", 6)], "Sea"),
        CreatureCard("Zombie",    [("Undead Bite", 6), ("Grave Stench", 5)], "Undead"),
        CreatureCard("Siren",     [("Melodic Charm", 7), ("Drowning Song", 6)], "Water"),
        CreatureCard("Pegasus",   [("Sky Strike", 7), ("Gale Wind", 6)], "Air"),
        CreatureCard("Dragon",    [("Blazing Fury", 9), ("Wing Gust", 6)], "Fire"),
        CreatureCard("Gargoyle",  [("Stone Gaze", 6), ("Granite Slam", 7)], "Earth"),
        CreatureCard("Archangel", [("Divine Light", 8), ("Winged Fury", 7)], "Light"),
        CreatureCard("Goblin",    [("Sneak Attack", 5), ("Nimble Strike", 6)], "Earth"),
        CreatureCard("Gollum",    [("Cunning Ambush", 7), ("Twisted Pummel", 6)], "Dark"),
    ]
    enhancements = [
        EnhancementCard("Mystic Forest",   "+2 Defense to all creatures"),
        EnhancementCard("Volcanic Terrain","+3 Attack to Fire creatures"),
    ]
    deck = creatures * 4 + enhancements * 2
    random.shuffle(deck)
    return deck

def battle(player1, player2):
    c1 = player1.play_creature()
    c2 = player2.play_creature()
    if not (c1 and c2):
        return

    print(f"{player1.name}'s {c1.name} battles {player2.name}'s {c2.name}!")
    # Minimal sample resolution: highest random attack wins (placeholder)
    a1 = random.choice(c1.attacks)
    a2 = random.choice(c2.attacks)
    print(f"{c1.name} uses {a1[0]} ({a1[1]} dmg)")
    print(f"{c2.name} uses {a2[0]} ({a2[1]} dmg)")
    if a1[1] > a2[1]:
        print(f"{c1.name} wins!\n")
    elif a1[1] < a2[1]:
        print(f"{c2.name} wins!\n")
    else:
        print("It's a draw!\n")

# Game Setup (up to 4 players)
player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
players = [Player(name) for name in player_names]
for p in players:
    p.deck = create_deck()

# Draw phase (one round)
for _ in range(5):
    for p in players:
        p.draw_card()

# Optional: each player tries to play an enhancement
for p in players:
    p.play_enhancement()

# Battle phase for each pair of players
for i in range(len(players) - 1):
    for j in range(i + 1, len(players)):
        battle(players[i], players[j])
