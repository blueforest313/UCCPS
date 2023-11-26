import sys

sys.stdin = open('phonein.txt', 'r')
sys.stdout = open('phoneout.txt', 'w')

n = int(input())
data = [[int(x) for x in input().split()] for i in range(0, n)]

left_min = [0]*n
right_min = [0]*n

left_min[-1] = data[-1][0]
right_min[-1] = 0

for i in range(2, n+1):
    left_min[-i] = min(right_min[-i+1] + data[-i][0],
                       left_min[-i+1] + data[-i][1] + data[-i][2])
    right_min[-i] = min(left_min[-i+1] + data[-i][2],
                        right_min[-i+1] + data[-i][1] + data[-i][0])

print(left_min[0])

# for i in range(0,n-1):
#     line = input().split(' ')
#     left_travel.insert(0, int(line[0]))
#     transfer.insert(0, int(line[1]))
#     right_travel.insert(0, int(line[2]))
# transfer.insert(0, int(input()))
#
# for i in range(1, n):
#     left_min[i] = min(right_min[i-1] + left_travel[i-1],
#                       left_min[i-1] + transfer[i] + right_travel[i-1])
#     right_min[i] = min(left_min[i-1] + right_travel[i-1],
#                        right_min[i-1] + transfer[i] + left_travel[i-1])
#
# print(left_min[n-1])


# create two lists, one for left-minimum time, one for
# right-minimum time. length = n
# create left-travel speed list, right-travel speed list, transfer list
# left_min[k] = min(left[k-1] + left_travel[k-1] + transfer[k-1], right[k-1] + tranfer[k-2] + right[k-1])
