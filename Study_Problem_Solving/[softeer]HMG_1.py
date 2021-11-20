from collections import defaultdict

def solution(room_names, room_times):
    room_dic = {}

    for room_name in room_names:
        room_dic[room_name] = [True] * 10

    for room_time in room_times:
        name, start, end = room_time[0], int(room_time[1]), int(room_time[2])
        for i in range(start - 9, end - 9):
            room_dic[name][i] = False

    time_dic = defaultdict(list)

    for key, values in room_dic.items():
        start_time = 0
        end_time = 0
        flag = False

        for i in range(len(values)):
            if values[i] is True:
                if start_time != 0:
                    continue
                else:
                    start_time = i + 9
            else:
                if start_time != 0:
                    flag = True
                    end_time = i + 9
                    time_dic[key].append([start_time, end_time])
                    start_time, end_time = 0, 0
                else:
                    continue
        if start_time != 0 and start_time != 18:
            flag = True
            time_dic[key].append([start_time, 18])

        if flag is False:
            time_dic[key] = []

    sort_dic = sorted(time_dic.items(), key = lambda x : x[0])
    display(sort_dic)

def display(sort_dic):
    count = 0
    for key, values in sort_dic:

        print("Room " + key + ":")
        if len(values) == 0:
            print("Not available")
        else:
            print(str(len(values)) + " available:")
            for value in values:
                start, end = value[0], value[1]
                if start // 10 == 0:
                    start = "0" + str(start)
                if end // 10 == 0:
                    end = "0" + str(end)
                print(str(start) + "-" + str(end))
        count += 1

        if count < len(sort_dic):
            print("-----")

if __name__ == "__main__":
   N, M = map(int, input().split())
   room_names = [input() for _ in range(N)]
   room_times = [list(map(str, input().split())) for _ in range(M)]

   solution(room_names, room_times)