class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            min_cost.append(min(min_cost[i-1], min_cost[i-2]) + cost[i])
        
        print(min_cost)
        return min(min_cost[n-1], min_cost[n-2])