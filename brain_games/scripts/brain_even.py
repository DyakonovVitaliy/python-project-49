#!/usr/bin/env python3
from brain_games.engine import logic
from brain_games.games.even import get_even, TASK


def main():
    logic(get_even, TASK)


if __name__ == '__main__':
    main()
