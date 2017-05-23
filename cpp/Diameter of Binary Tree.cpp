/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int result = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return result;
    }

    int depth(TreeNode *root) {
        if (!root)
            return 0;
        else {
            int left_depth = depth(root->left);
            int right_depth = depth(root->right);
            result = max(result, left_depth + right_depth);
            return max(left_depth, right_depth) + 1;
        }
    }

};
