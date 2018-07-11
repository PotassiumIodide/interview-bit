/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int check(TreeNode* ln ,TreeNode* rn){
    if(ln==NULL && rn==NULL)
    return 1;
    
    else if((ln ==NULL && rn!=NULL)||(ln!= NULL && rn==NULL))
    return 0;
    
    else if(ln->val==rn->val){
        return min(check(ln->left,rn->right),check(ln->right,rn->left));
    }
    return 0;
    
    
    
}
int Solution::isSymmetric(TreeNode* A) {
    if (A==NULL)
    return 1;
    
    return check(A->left,A->right);
}
