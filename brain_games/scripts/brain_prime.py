#!/usr/bin/env python3
from brain_games.engine import logic
from brain_games.games.prime import get_prime, the_task


def main():
    logic(get_prime, the_task)


if __name__ == '__main__':
    main()
