"""
Best Time to Buy and Sell Stock
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        min_price = sys.maxsize

        for price in prices:
            answer = max(answer, price - min_price)

            if price < min_price:
                min_price = price

        return answer

if __name__=="__main__":
    solution = Solution()
    prices1 = [7,1,5,3,6,4]
    prices2 = [2,4,1]
    print(solution.maxProfit(prices1))
    print(solution.maxProfit(prices2))