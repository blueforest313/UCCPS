import sys


def mango(i, c, i_man, c_man) -> int:
    distances = [int(i)+int(i_man), int(i)-int(i_man), int(c)+int(c_man), int(c)-int(c_man)]
    for element in set(distances):
        distances.remove(element)
    return distances.pop()


sys.stdin = open('manin.txt', 'r')
sys.stdout = open('manout.txt', 'w')
a,b,c,d = [int(x) for x in input().split(' ')]

print(mango(a,b,c,d))
