import sys


def min_instructions(n:int, init_instr: str) -> int:
    vertical = 0
    horizontal = 0
    for i in range(0,n):
        direction = init_instr[i]
        if direction == 'N':
            vertical += 1
        elif direction == 'S':
            vertical -= 1
        elif direction == 'W':
            horizontal += 1
        else:
            horizontal -= 1
    return abs(vertical) + abs(horizontal)


sys.stdin = open('robotin.txt', 'r')
sys.stdout = open('robotout.txt', 'w')

number_instr = input()
instructions = input()

print(min_instructions(int(number_instr), instructions))
