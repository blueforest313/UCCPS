n = int(input())
array_int = input()

integers = [int(m) for m in array_int.split(' ')]

mnass_list = [0]*(n+1)
mnass_list[1] = integers[0]

for i in range(2,n+1):
    mnass_list[i] = max(integers[i-1]+ max(mnass_list[i-2], 0), mnass_list[i-1])

print(max(mnass_list[n], 0))
