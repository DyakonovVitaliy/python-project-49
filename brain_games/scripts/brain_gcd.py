#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.gcd import get_gcd, TASK


def main():
    start_game(get_gcd, TASK)


if __name__ == '__main__':
    main()
