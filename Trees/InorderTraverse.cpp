/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
    vector<int> Solution::inorderTraversal(TreeNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    vector<int> sol;
    stack<TreeNode*> st;
    
    TreeNode* curr = A;
    while(curr!=NULL || st.empty()==false){
        while(curr!=NULL){
            st.push(curr);
            curr=curr->left;
        }
        curr= st.top();
        sol.push_back(st.top()->val);
        st.pop();
        curr=curr->right;
    }
    return sol;
}

