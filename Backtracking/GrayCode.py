class Solution:
    # @param A : integer
    # @return a list of integers
    res = ["0", "1"]
    def grayCodeUtil(self, k , n) :
        #global res
        if k == n :
            return self.res
        else :
            L1 = self.res[:]
            L2 = L1[:]
            L2.reverse()
            for i in range(len(L1)) :
                L1[i] = "0" + L1[i]
            for i in range(len(L2)) :
                L2[i] = "1" + L2[i]
            self.res = L1 + L2
        #print res
            self.grayCodeUtil(k+1, n)
    def grayCode(self, A):
        #global res
        self.grayCodeUtil(1, A)
        arr=[]
        for i in range(len(self.res)):
            Sum =0
            for j in range(len(self.res[i])):
                Sum =Sum +int(self.res[i][len(self.res[i])-j-1])*(2**j)
            arr.append(Sum)
        return arr
                
                
        
