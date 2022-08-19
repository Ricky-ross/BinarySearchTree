from typing import List


class Solution:
    def solve(self, N: int, A: List[int]) -> int:
        # code here
        a = A
        a.sort()
        n = N
        count = 0
        for i in range(n):
            if i == 0:
                count = count + 1
            else:
                if a[i] == a[i - 1]:
                    count = count + 1
                elif a[i] == a[i - 1] + 1:
                    count = count + 1
        return count

s = 5
arr = [1,2,3,2,4]
sol = Solution()
print(sol.solve(s,arr))