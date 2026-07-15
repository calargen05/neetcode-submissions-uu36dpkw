'''

NAIVE SOLUTION:

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)

        runs = []

        # for loop that tests each value of k from 1 to m
        for i in range(1,m+1):
            h_needed = 0    # Hours needed to finish a pile
            for p in piles:
                h_needed += math.ceil(p/i)  # incrementing the hours needed to finish a pile
                # checks if the hours needed is greater than the allotted hours
                if h_needed > h:
                    break
            # appends a possible minimum to the list of possible minimums
            if h_needed <= h:
                runs.append(i)
        
        return min(runs)

'''

# BINARY SEARCH

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        runs = []

        min_eat = r

        while l <= r:           
            mid = (l + r) // 2
            h_needed = 0
            for p in piles:
                h_needed += math.ceil(p/mid)
                if h_needed > h:
                    break
            if h_needed <= h:
                min_eat = min(min_eat,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_eat
            