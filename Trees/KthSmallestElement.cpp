/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int Solution::kthsmallest(TreeNode* root, int k) {
    
    if(root == NULL){
        return -1;
    }
    
    vector<int> sol;
    stack<TreeNode*> st;
    TreeNode* curr = root;
    while(curr!=NULL || st.empty()==false){
        while(curr!=NULL){
            st.push(curr);
            curr=curr->left;
        }
        curr =st.top();
        sol.push_back(curr->val);
        st.pop();
        curr=curr->right;
    }
    return sol[k-1];
    
}
