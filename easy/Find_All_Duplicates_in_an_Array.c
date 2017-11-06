/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    bool mark[numsSize+1];
    memset(mark, 0, numsSize+1);
    for(int i = 0; i < numsSize; i++)
        mark[nums[i]] = true;
    
    int n = 0;    
    for(int i = 1; i < numsSize+1; i++)
        n += (mark[i])?0:1;
    *returnSize = n;
    
    int *arr = (int*)malloc(sizeof(int) * *returnSize);
    int p = 0;
    for(int i = 1; i < numsSize+1; i++)
        if(!mark[i])
            arr[p++] = i;
    return arr;
}