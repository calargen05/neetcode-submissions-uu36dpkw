class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case
        if len(s) == 0: return 0

        # hash table to keep track of counted characters
        hashtable = {}

        # left and right pointers for the sliding window and result variable
        l, r, res = 0, 0, 1

        # loop for sliding window algorithm to check for the longest substring
        while r < len(s):
            # checking if the character has been encountered already
            if s[r] in hashtable:
                # checking if the current substring is the biggest we've encountered
                if len(hashtable) > res:
                    res = len(hashtable)
                # clear the hashtable for the next substring and move the starting pointer for the sliding window
                hashtable.pop(s[l])
                l += 1
            else:
                # append the new character to the hashtable and increment the right pointer by 1
                hashtable[s[r]] = 1
                r+=1
        # do one more check for the length of the current substring 
        # in the case that the loop ended before it could be checked
        # by the if statements in the loop
        if len(hashtable) > res: res = len(hashtable)
        return res