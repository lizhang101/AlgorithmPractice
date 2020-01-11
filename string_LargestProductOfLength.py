class Solution(object):
    def largestProduct(self, dict):
        """
        input: string[] dict
        return: int
        """
        # write your solution here
        if len(dict) <= 1:
            return len(dict)
        words = sorted(dict, key=len, reverse=True)
        l = 0
        s = 1
        while s < len(words) and l < len(words) - 1:
            if len(set(words[s]) & set(words[l])) == 0:
                return len(words[s]) * len(words[l])
            else:
                if s == l + 1:
                    s += 1
                else:
                    l += 1
        return 0
