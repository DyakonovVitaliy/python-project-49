#!/usr/bin/env python3
from brain_games.engine import logic
from brain_games.games.progression import get_progression, the_task


def main():
    logic(get_progression, the_task)


if __name__ == '__main__':
    main()
