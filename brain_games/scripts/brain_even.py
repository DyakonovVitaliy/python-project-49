#!/usr/bin/env python3
#!/usr/bin/env python3
from brain_games.engine import logic
from brain_games.games.even import get_even, the_task

def main():
    logic(get_even, the_task)


if __name__ == '__main__':
    main()