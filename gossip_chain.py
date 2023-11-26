n = input()

connected_string = 'j for j in range(0, n)'

line = input()
while line != '-1 -1':
    connected_string.replace(line[0], line[1])
    line = input()

new_line = input()
while line != '-1 -1':
    if connected_string[int(line[0])] == connected_string[int(line[1])]:
        print('yes')
    else:
        print('no')
