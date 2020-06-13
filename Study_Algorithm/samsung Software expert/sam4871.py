if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        v, e = map(int, input().split())
        e_arr = []
        Stack = []
        for element in range(1,e+1):
            temp = list(map(int, input().split()))
            e_arr.append(temp)
        S, G = map(int, input().split())
        temp_S = S
        temp_G = G
        for item in e_arr:

            if item[0] == temp_S:
                Stack.append(item)


        print(e_arr)
        print(S,G)