class Solution:
    def __init__(self,s):
        self.s = s

    def reverseString(self):
        self.s.reverse()

if __name__=="__main__":
    s1 = ['a','b','c','d']
    test = Solution(s1)
    test.reverseString()
    print(s1)