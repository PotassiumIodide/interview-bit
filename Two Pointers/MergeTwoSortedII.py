class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        
        i , j = 0, 0
        temp = A[:]
        A = []
        while i < len(temp) and j < len(B) :
            if temp[i] > B[j] :
                A.append(B[j])
                j += 1
            else :
                A.append(temp[i])
                i += 1
        while i < len(temp) :
            A.append(temp[i])
            i += 1

        while j < len(B) :
            A.append(B[j])
            j += 1
        
        print " ".join(map(str, A)) + " "

                
                    
