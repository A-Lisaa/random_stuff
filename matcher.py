import random
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Player:
    name: str
    elo: int


def generate_players(amount: int, elo_range: tuple[int, int]) -> list[Player]:
    return [
        Player(
            f"Player {i}",
            random.randint(elo_range[0], elo_range[1])
        )
        for i in range(1, amount+1)
    ]


def generate_random_pairs(players: list[Player]):
    pairs = [(player1, player2) for player2 in players for player1 in players]
    random.shuffle(pairs)
    return pairs


def create_table(players: list[Player], games_per_day: int) -> list[list[tuple[Player, Player]]]:
    if len(players) % games_per_day != 0:
        print(f"Players ({len(players)}) can not be divided with {games_per_day} games per day.")

    pairs = generate_random_pairs(players)
    return [pairs[games_per_day*(i-1):games_per_day*i] for i in range(1, len(pairs) // games_per_day + 1)]


def main():
    players = generate_players(8, (2700, 2800))
    print(*players, sep="\n")
    pairs = create_table(players, 4)
    print(*pairs, sep="\n")


if __name__ == "__main__":
    main()
