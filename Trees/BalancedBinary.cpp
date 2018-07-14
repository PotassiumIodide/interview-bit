/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 int helper(TreeNode* root){
     
     if(root==NULL)
     return 1;
     
     else if(root->left==NULL && root->right==NULL)
     return 1;
     
     else if(root->left!=NULL && root->right!=NULL)
     return min(helper(root->left),helper(root->right));
     
     else if(root->left!=NULL && root->right==NULL){
         TreeNode* temp =root->left;
         if(temp->left!=NULL || temp->right!=NULL)
         return 0;
     }
     else if(root->left==NULL && root->right!=NULL){
         TreeNode* temp =root->right;
         if(temp->left!=NULL || temp->right!=NULL)
         return 0;
     }
     return 1;
     
 }
int Solution::isBalanced(TreeNode* A) {
    return helper(A);
}
