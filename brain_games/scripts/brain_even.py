#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.even import get_even, TASK


def main():
    start_game(get_even, TASK)


if __name__ == '__main__':
    main()
