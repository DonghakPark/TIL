import collections
from typing import List

def solution(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

if __name__ =="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    answer = [["bat"],["nat","tan"],["ate","eat","tea"]]

    if answer == solution(strs):
        print("Correct")
    else:
        print("Wrong")