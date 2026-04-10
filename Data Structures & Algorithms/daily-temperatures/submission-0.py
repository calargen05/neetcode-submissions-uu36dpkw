class Solution:

    """
        for loop to loop through temperatures:
            if the rest of the list doesn't have a hotter temp:
                append 0 to the result list
            else:
                find the index of the first hotter temp and find the difference between the indexes
        return result list
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            if max(temperatures[i:]) == temperatures[i]:
                res.append(0)
            else:
                for j in range(i, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        res.append(j-i)
                        break
        
        return res