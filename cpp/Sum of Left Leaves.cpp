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
    int sum = 0;
    int sumOfLeftLeaves(TreeNode* root) {
        find(root);
        return sum;
    }

    bool is_leaf(TreeNode* node) {
        return node->left == NULL && node->right == NULL;
    }

    void find(TreeNode* root) {
        if (!root) {
            return;
        }
        if (root->left != NULL && is_leaf(root->left)) {
            sum += root->left->val;
        } else {
            find(root->left);
        }
        find(root->right);
    }
};
