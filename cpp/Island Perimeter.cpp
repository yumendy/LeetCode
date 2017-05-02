class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        unsigned int width = grid[0].size();
        vector<int> first_line = vector<int>(width, 0);
        vector<int> last_line = vector<int>(width, 0);
        grid.push_back(last_line);
        grid.insert(grid.begin(), first_line);

        for(int i = 0; i < grid.size(); i++) {
            grid[i].push_back(0);
            grid[i].insert(grid[i].begin(), 0);
        }

        int counter = 0;
        for (int row = 1; row < grid.size() -1; ++row) {
            for (int col = 1; col < width + 1; ++col) {
                if (grid[row][col]) {
                    if (!grid[row - 1][col])
                        counter++;
                    if (!grid[row + 1][col])
                        counter++;
                    if (!grid[row][col - 1])
                        counter++;
                    if (!grid[row][col + 1])
                        counter++;
                }
            }
        }
        return counter;
    }
};
