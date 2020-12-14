sorted_num = [1,2,3,4,5,6,7,8]
reversed_num = [8,7,6,5,4,3,2,1]

target = list(map(int, input().split()))

if target == sorted_num:
    print("ascending")
elif target == reversed_num:
    print("descending")
else:
    print("mixed")