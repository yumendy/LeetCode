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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        queue<pair<TreeNode*, size_t >> q;
        q.push(pair<TreeNode*, size_t >(root, 1));
        vector<vector<int>> result_list;

        while (!q.empty()) {
            pair<TreeNode*, size_t > p = (pair<TreeNode *, size_t> &&) q.front();
            q.pop();
            if (p.first) {
                if (result_list.size() < p.second) {
                    vector<int> temp;
                    result_list.push_back(temp);
                }
                result_list[p.second - 1].push_back(p.first->val);
                if (p.first->left)
                    q.push(pair<TreeNode*, size_t >(p.first->left, p.second + 1));
                if (p.first->right)
                    q.push(pair<TreeNode*, size_t >(p.first->right, p.second + 1));
            }
        }
        reverse(result_list.begin(), result_list.end());
        return result_list;
    }
};
