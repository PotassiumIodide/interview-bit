long long int sum(vector<int>&arr){
    long long int summ=0;
    for(int i=0;i<arr.size();i++){
        summ +=arr[i];
    }
    return summ;
    
}
vector<int> Solution::maxset(vector<int> &A) {
    
    long long int i,j,maxsum=-1;
    vector<int>arr;
    vector<int>ans;
    for (i= 0;i<A.size();i++){
        if (A[i]<0){
            if (!arr.empty()){
                if (sum(arr)>maxsum){
            ans =arr;
            maxsum =sum(arr);
            }
            arr.clear();
            }
            
        }
        
        if (A[i]>=0){
            arr.push_back(A[i]);
        }
        
            
        }
        
        if (sum(arr)>maxsum)
            ans =arr;
        
    return ans;
    
    
       
}


