/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(root == NULL)
        return 0;
    
    if(root->left == NULL && root->right == NULL)
        return 1;
    
    int left_len = 0, right_len = 0;    
    
    if(root->left != NULL)
        left_len = maxDepth(root->left);
    if(root->right != NULL)
        right_len = maxDepth(root->right);
        
    return 1 + ((left_len > right_len)? left_len : right_len);    
}