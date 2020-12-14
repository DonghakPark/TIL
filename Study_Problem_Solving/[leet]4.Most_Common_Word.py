import re
import collections
from typing import List

def solution(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

if __name__=="__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    answer = 'ball'

    if answer == solution(paragraph, banned):
        print("Correct")
    else:
        print("Wrong")