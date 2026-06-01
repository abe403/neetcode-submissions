class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowseen = [set() for _ in range(len(board))]
        colseen = [set() for _ in range(len(board))]
        blockseen = [set() for _ in range(len(board))]

        for i in range(len(board)):
            
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                if board[i][j] not in rowseen[i]:
                    rowseen[i].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in colseen[j]:
                    colseen[j].add(board[i][j])
                else:
                    return False

                block_index = (i // 3) * 3 + (j // 3)

                if board[i][j] not in blockseen[block_index]:
                    blockseen[block_index].add(board[i][j])
                else:
                    return False
            
        return True