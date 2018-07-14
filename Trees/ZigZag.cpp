/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
void helper(TreeNode* root,vector<vector<int>>&sol,bool ltr,int level){
    if(root== NULL)
    return;
    
    if(sol.size()<level){
        vector<int>temp;
        sol.push_back(temp);
    }
    
    if(ltr){
        sol[level-1].push_back(root->val);
    }
    
    else{
        sol[level-1].insert(sol[level-1].begin(),root->val);
    }
    helper(root->left,sol,!ltr,level+1);
    helper(root->right,sol,!ltr,level+1);
    
}
vector<vector<int> > Solution::zigzagLevelOrder(TreeNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    vector<vector<int>>sol;
    helper(A,sol,true,1);
    return sol;
}
