import sys


def min_notes(n:int) -> int:
    number_notes = 0
    notes = [100, 20, 5, 1]
    while n > 0:
        for i in range(0,4):
            if n >= notes[i]:
                number = (n//notes[i])
                n -= number*notes[i]
                number_notes += number
    return number_notes


sys.stdin = open('fashin.txt', 'r')
sys.stdout = open('fashout.txt', 'w')

print(min_notes(int(input())))
