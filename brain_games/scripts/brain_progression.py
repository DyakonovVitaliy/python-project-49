#!/usr/bin/env python3
from brain_games.engine import logic
from brain_games.games.progression import get_progression, TASK


def main():
    logic(get_progression, TASK)


if __name__ == '__main__':
    main()
