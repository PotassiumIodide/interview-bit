vector<int> Solution::dNums(vector<int> &A, int B) {
    vector<int>ans;
    if (A.size()<B){
    return ans;
    }
    
    map<int,int>dict;
    int unique =0;
    
    for(int i=0;i<B;i++){
        auto it =dict.find(A[i]);
        if (it==dict.end()){
            dict[A[i]]=1;
            unique++;
        }
        else{
            it->second++;
        }
    }
    ans.push_back(unique);
    
    for(int i=B;i<A.size();i++){
        auto it =dict.find(A[i-B]);
        if (it->second==1){
            dict.erase(it);
            unique--;
        }
        else{
            it->second--;
        }
        
        auto temp =dict.find(A[i]);
        if (temp==dict.end()){
            dict[A[i]]=1;
            unique++;
            
        }
        else{
            temp->second++;
        }
        
        ans.push_back(unique);
    }
    return ans;
    

}
