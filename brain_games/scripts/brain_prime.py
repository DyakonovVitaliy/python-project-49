#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.prime import get_prime, TASK


def main():
    start_game(get_prime, TASK)


if __name__ == '__main__':
    main()
