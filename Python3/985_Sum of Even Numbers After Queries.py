class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        ret = []
        
        even_sum = sum(x for x in A if x % 2 == 0)

        
        for q in queries:
            index = q[1]
            
            if A[index] % 2 == 0:
                even_sum -= A[index]
            
            A[index] += q[0]
            
            if A[index] % 2 == 0:
                even_sum += A[index]
            
            ret.append(even_sum)
        return ret
