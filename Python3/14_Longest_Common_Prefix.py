class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        j = 0
        while True:
            try:
                p = strs[0][j]
                for s in strs:
                    if s[j] == p:
                        continue
                    else:
                        return ''.join(prefix)
                prefix.append(p)
            except Exception:
                return ''.join(prefix)
            j += 1

# Beat 92%
