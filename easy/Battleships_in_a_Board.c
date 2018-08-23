

int countBattleships(char** board, int boardRowSize, int boardColSize) {
    int cnt = 0;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    for(int i = 0; i < boardRowSize; i++)
    {
        for(int j = 0; j < boardColSize; j++)
        {
            if(board[i][j] == 'X')
            {
                cnt++;
                board[i][j] = 0;
                for(int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    
                    if(nx < 0 || ny < 0 || nx >= boardRowSize || ny >= boardColSize)
                        continue;
                    
                    while(board[nx][ny] == 'X')
                    {
                        board[nx][ny] = 0;
                        nx += dx[k];
                        ny += dy[k];
                        if(nx < 0 || ny < 0 || nx >= boardRowSize || ny >= boardColSize)
                            break;
                    }
                }
            }
        }
    }
    return cnt;
}