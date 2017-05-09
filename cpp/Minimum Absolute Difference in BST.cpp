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
    int min_diff = INFINITY;
    int prev = INFINITY;
    int getMinimumDifference(TreeNode* root) {
        get_min(root);
        return min_diff;
    }

    void get_min(TreeNode* tree) {
        if (tree) {
            get_min(tree->left);
            min_diff = min(min_diff, abs(prev - tree->val));
            prev = tree->val;
            get_min(tree->right);
        }
    }
};
