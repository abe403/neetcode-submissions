class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> columns;
        unordered_map<int, unordered_set<char>> blocks;

        for (int r=0; r < board.size(); r++) {
            for (int c=0; c < board.size(); c++) {
                char cur = board[r][c];

                if (cur == '.') {
                    continue;
                }
                
                bool isRowDuplicate = !rows[r].insert(cur).second;
                if (isRowDuplicate) {
                    return false;
                }
                
                bool isColumnDuplicate = !columns[c].insert(cur).second;
                if (isColumnDuplicate) {
                    return false;
                }

                int block = ((c/3) * 3) + (r/3);

                bool isBlockDuplicate = !blocks[block].insert(cur).second;
                if (isBlockDuplicate) {
                    return false;
                }
            }
        }
        return true;
    }
};