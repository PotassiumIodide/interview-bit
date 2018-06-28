class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        arr =[]
        while A!=0:
            arr.insert(0,A%10)
            A =A//10
    
        dic = {}
        for i in range(len(arr)):
            value =1
            for j in range(i,len(arr)):
                value =value*arr[j]
                if dic.get(value) !=None:
                    return 0
                dic[value]=value
        return 1
