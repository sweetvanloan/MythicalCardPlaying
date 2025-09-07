from .engine import start_game, round_robin_battles

def print_board(state):
    print("\n=== BOARD ===")
    for p in state.players:
        enh = ", ".join(e.name for e in p.board_enhancements) or "None"
        if p.active_creature:
            c = p.active_creature
            print(f"{p.name}: {c.name} [{c.ctype.name}] HP {c.hp}/{c.max_hp} | Enhancements: {enh}")
        else:
            print(f"{p.name}: No active creature | Enhancements: {enh}")
    print("=============\n")

def main():
    # Change num_players to 2, 3, or 4
    state = start_game(num_players=4, seed=1337)

    print_board(state)
    logs = round_robin_battles(state)
    for line in logs:
        print(line)
    print_board(state)

if __name__ == "__main__":
    main()
