import numpy as np
import re


def main():
    with open('day08.txt') as f:
        instructions = [line.strip() for line in f]
    print(solve(instructions))


def solve(instructions):
    width, height = 50, 6
    screen = [[' ' for _ in range(width)] for _ in range(height) ] 
    plot(screen)

    for inst in instructions:
        val1, val2 = map(int, re.findall(r"\d+", inst))
        if inst.startswith('rect'):
            print(val1, val2)
            for i in range(val2):
                for j in range(val1):
                    screen[i][j] = '#'
        elif inst.startswith('rotate row'):
            screen[val1] = list(np.roll(np.array(screen[val1]), val2))

        elif inst.startswith('rotate col'):
            tmp = [row[val1] for row in screen]
            tmp = list(np.roll(np.array(tmp), val2))
            for i, c in enumerate(tmp):
                screen[i][val1] = c

    plot(screen)
    lit = 0
    for row in screen:
        for c in row:
            if c == '#':
                lit += 1
    return lit


def plot(screen):
    for row in screen: 
        line = ""
        for c in row: 
            line += c
        print(line)
    print()


if __name__ == '__main__':
    main()
