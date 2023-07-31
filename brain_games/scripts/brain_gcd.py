#!/usr/bin/env python3
from brain_games.engine import logic
from brain_games.games.gcd import get_gcd, TASK


def main():
    logic(get_gcd, TASK)


if __name__ == '__main__':
    main()
