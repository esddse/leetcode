int islandPerimeter(int** grid, int gridRowSize, int gridColSize) {
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int total = 0;
    for(int i = 0; i < gridRowSize; i++)
    {
        for(int j = 0; j < gridColSize; j++)
        {
            if(grid[i][j] == 0)
                continue;
                
            int cnt = 0;
            for(int k = 0; k < 4; k++)
                if(i+dx[k] >= 0 && i+dx[k] < gridRowSize && j+dy[k] >= 0 && j+dy[k] < gridColSize)
                    cnt += (grid[i+dx[k]][j+dy[k]] == 1)? 0 : 1;
                else 
                    cnt += 1;
            total += cnt;
        }
    }
    return total;
}