def check_end():
    global Arr_people

    for key in Arr_people.keys():
        if Arr_people[key] and final_people[key] is False:
            return False
    return True

N = int(input())
Arr_people = {}
Arr_item = {}
final_item = {}
final_people = {}

for _ in range(N):
    item_name, order, item_number = map(str, input().split())
    Arr_item[item_name] = [order, int(item_number)]
    final_item[item_name] = []

M = int(input())

for _ in range(M):
    people_name, order, wanted_number = map(str, input().split())
    Arr_people[people_name] = list(order)[:int(wanted_number)]
    final_people[people_name] = False

while True:
    if check_end():
        break

    for key in Arr_people.keys():
        if Arr_people[key] and final_people[key] is False:
            temp = Arr_people[key].pop(0)
            final_item[temp].append(key)

    for key in final_item.keys():
        if final_item[key]:
            temp = []
            for element in final_item[key]:
                for i in range(len(Arr_item[key][0])):
                    if element == Arr_item[key][0][i]:
                        temp.append([i,element])
            temp.sort(reverse=True)
            while len(final_item[key]) > Arr_item[key][1]:
                _, element = temp.pop(0)
                final_item[key].remove(element)
                final_people[element] = False

            for element in final_item[key]:
                final_people[element] = True
for key in final_item.keys():
    final_item[key].sort()
    print(key + "_" + "".join(final_item[key]))