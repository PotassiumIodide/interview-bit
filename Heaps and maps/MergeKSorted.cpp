/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    map<int,int>dict;
    for(int i=0;i<A.size();i++){
        while(A[i]!=NULL){
            auto it  =dict.find(A[i]->val);
            if (it==dict.end()){
                dict[A[i]->val]=1;
            }
            else{
                it->second++;
            }
            A[i] =A[i]->next;
        }
    }
    
    auto it =dict.begin();
    ListNode *head=NULL;
    ListNode *curr=NULL;
    
    while(it!=dict.end()){
        while(it->second != 0){
            ListNode* list = new ListNode(it->first);
            if(head == NULL){
                head = list;
                curr = list;
            }
            else{
                curr->next = list;
                curr = curr->next;
            }
            it->second--;
        }
        it++;
    }
    
    return head;
    
    
}
