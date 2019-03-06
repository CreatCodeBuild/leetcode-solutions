# array/string - 次数 -> hash map
# hash map - 顺序 -> Priority Queue
# Priority Queue - 重组 -> array/string

# https://leetcode.com/problems/reorganize-string
import heapq
from math import ceil

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        counter = {}
        for c in S:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
                
        q = []
        for c, count in counter.items():
            if count > ceil(len(S)/2):
                return ''
            heapq.heappush(q, [-count, c])
            
        ret = []
        while len(q) >= 2:
            
            e1 = heapq.heappop(q)
            e2 = heapq.heappop(q)
            ret.extend([e1[1], e2[1]])
            
            if e1[0] < -1:
                e1[0] += 1
                heapq.heappush(q, e1)
                
            if e2[0] < -1:
                e2[0] += 1
                heapq.heappush(q, e2)
        
        if len(q) == 1:
            ret.append(q[0][1])
        
        return ''.join(ret)
        
