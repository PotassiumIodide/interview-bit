class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        
        res = ""
        i, j, k, c = len(A) - 1, len(B) - 1 , 0, 0
        while i >= 0 and j >= 0 :
            if int(A[i]) + int(B[j])+ c == 2 :
                c = 1
                res = '0' + res
            elif int(A[i]) + int(B[j]) +c == 3:
                c = 1
                res = '1' + res
            elif int(A[i]) + int(B[j]) +c == 1:
                c =0
                res = '1' + res
            elif int(A[i])+int(B[j])+c==0:
                res = '0'+res
                c = 0
            i -= 1
            j -= 1
        while i >= 0 :
            if int(A[i]) + c == 2 :
                c = 1
                res = '0' + res
            else :
                res = str(int(A[i]) + c) + res
                c = 0
            i -= 1

        while j >= 0 :
            if int(B[j]) + c == 2 :
                c = 1
                res = '0' + res
            else :
                res = str(int(B[j]) + c) + res
                c = 0
            j -= 1
        if c == 1 :
            res = '1' + res
        return res
