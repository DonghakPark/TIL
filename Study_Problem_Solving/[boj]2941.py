"""
크로아티아 알파벳 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

S = input()
S = S.replace("c=", '1')
S = S.replace("c-", '1')
S = S.replace("dz=", '1')
S = S.replace("d-", '1')
S = S.replace("lj", '1')
S = S.replace("nj", '1')
S = S.replace("s=" , '1')
S = S.replace("z=" , '1')

print(len(S))