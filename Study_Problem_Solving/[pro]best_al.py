from collections import defaultdict


def solution(genres, plays):
    answer = []
    dict_song = defaultdict(list)

    for i in range(len(genres)):
        dict_song[genres[i]].append([plays[i], i])

    famous_genres = []
    for key in dict_song.keys():
        temp_sum = 0
        for song, index in dict_song[key]:
            temp_sum += song
        famous_genres.append([temp_sum, key])

    famous_genres.sort(key=lambda x: -x[0])

    for element in famous_genres:
        if len(dict_song[element[1]]) < 2:
            answer.append(dict_song[element[1]][0][1])
        else:
            dict_song[element[1]].sort(key=lambda x: (-x[0], x[1]))
            answer.append(dict_song[element[1]][0][1])
            answer.append(dict_song[element[1]][1][1])

    return answer