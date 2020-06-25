import re
import math

def solve_data():

    data = []

    fd = open("A.dat", 'r', encoding="utf-8")
    string_data = " ".join(fd.readlines())

    p = re.compile(r"(\d+),(\d+):(\d+)|(\d+),(\d+):(-\d+)")
    result = p.findall(string_data)
    for element in result:
        temp = list(element)
        temp.remove('')
        temp.remove('')
        temp.remove('')
        temp = list(map(int, temp))
        data.append(temp)
    return data

def find_size(data):
    max_row = sorted(data, key = lambda x: x[0], reverse=True)
    max_col = sorted(data, key = lambda x: x[1], reverse=True)
    return max_row[0][0], max_col[0][1]

def find_value(data):
    max_value = sorted(data, key = lambda x : x[2], reverse = True)
    min_value = max_value[-1][2]
    return max_value[0][2], min_value

def comp_dist(data):
    row_10 = []
    row_27 = []
    dist = 0
    for element in data:
        if element[0] == 10:
            row_10.append(element)
        if element[0] == 27:
            row_27.append(element)
    row_10.sort()
    row_27.sort()
    for a,b in zip(row_10,row_27):
        dist += (a[2]-b[2])**2

    result = math.sqrt(dist)
    return result

def find_index(data, row1, row2):
    row_1 = []
    row_2 = []
    dist = 0
    for element in data:
        if element[0] == row1:
            row_1.append(element)
        if element[0] == row2:
            row_2.append(element)

    row_1.sort()
    row_2.sort()

    for a,b in zip(row_1, row_2):
        dist += (a[2]-b[2])**2
    result = math.sqrt(dist)

    return result

if __name__=="__main__":
    data = solve_data()

    max_row, max_col = find_size(data)
    print("max_row : {}, max_col : {}".format(max_row, max_col))

    max_value, min_value = find_value(data)
    print("max_value : {} mix_value : {}".format(max_value, min_value))

    Euclidean_dist = comp_dist(data)
    print("Euclidean_dist : {}".format(Euclidean_dist))

    print("below row is less then or equal to 10.0 to the 37 row")

    for row1 in range(0, max_row):
        temp_result = find_index(data,row1,37)
        if row1 == 37:
            continue
        elif temp_result <= 10.0:
            print("----row : {}".format(row1))
