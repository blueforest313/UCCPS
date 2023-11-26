import sys

sys.stdin = open('jogin.txt', 'r')
sys.stdout = open('jogout.txt', 'w')

landmarks = int(input())
# creating dictionary with in degrees & create adjacency list
degree_dict = {n: [] for n in range(1, landmarks + 1)}
in_degrees = [0]*landmarks

while True:
    code_line = input()
    numbers_list = code_line.split(' ')
    if numbers_list == ['0', '0', '0']:
        break
    else:
        degree_dict[int(numbers_list[0])].append([int(numbers_list[1]), int(numbers_list[2])])
        in_degrees[int(numbers_list[1])-1] += 1

degree_zero_nodes = []
for i in range(0,landmarks):
    if in_degrees[i] == 0:
        degree_zero_nodes.append(i+1)

benefit_list_outside = ['']*landmarks
top_order = []

while degree_zero_nodes:
    node = degree_zero_nodes.pop()
    top_order.append(node)
    connected_list = degree_dict[node]
    for new_node, value in connected_list:
        in_degrees[new_node-1] -= 1
        if in_degrees[new_node-1] == 0:
            degree_zero_nodes.append(new_node)


benefits = {n: 0 for n in top_order}


def maximal_benefit(a: dict, start_node: int, benefit_dict: dict) -> int:
    connected_list_inside = a[start_node]
    maximum = 0  # ensures maximum non-neg
    for node_inside, value_inside in connected_list_inside:
        if value_inside + benefit_dict[node_inside] > maximum:
            maximum = value_inside + benefit_dict[node_inside]
    return maximum


for n in top_order[::-1]:
    benefits[n] = maximal_benefit(degree_dict, n, benefits)

print(max(benefits[n] for n in benefits))



# def maximal_benefit(a: dict, start_node: int, benefit_list: list) -> int:
#     if not dict:
#         return 0
#     else:
#         connected_list = a.pop(start_node)
#         maximum = 0
#         for node, value in connected_list:
#             if value > 0:
#                 if benefit_list[node-1] == '':
#                     benefit_list[node-1] = compared_value = maximal_benefit(a, node, benefit_list)
#                 else:
#                     compared_value = benefit_list[node-1]
#
#                 comp_value = compared_value + max(0, value)
#                 if comp_value > maximum:
#                     maximum = comp_value
#         return maximum
