#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.calc import get_calc, TASK


def main():
    start_game(get_calc, TASK)


if __name__ == '__main__':
    main()
