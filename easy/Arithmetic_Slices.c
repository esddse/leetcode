int numberOfArithmeticSlices(int* A, int ASize) {
    int cnt = 0;
    for(int p = 0; p <= ASize-3; p++)
    {
        int a = A[p] - A[p+1];
        int b = A[p+1] - A[p+2];
        if(a != b)
            continue;
        cnt++;
        for(int q = p+3; q < ASize; q++)
        {
            if(A[q-1] - A[q] == a)
                cnt++;
            else 
                break;
        }
    }
    
    return cnt;
}