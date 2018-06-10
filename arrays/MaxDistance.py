class Solution:
    # @param A : tuple of integers
    # @return an integer
    def h(self, seq):
        return sorted(range(len(seq)), key=seq.__getitem__)
    
    def maximumGap(self, A):
        
        if len(A) == 0:
            return -1
        
        index_sort = self.h(A)
        
        max_dist = 0
        max_index_right = index_sort[len(A)-1]
        
        for i in range(len(A)-1, -1, -1):
            if index_sort[i] < max_index_right:
                max_dist = max(max_index_right-index_sort[i], max_dist)
            else:
                max_index_right = index_sort[i]
        
        return max_dist
