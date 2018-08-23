/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructRectangle(int area, int* returnSize) {
    *returnSize = 2;
    int* arr = (int*)malloc(sizeof(int)*2);
    int sqLen = sqrt(area);
    for(int w = sqLen; w > 0; w--)
    {
        if(area % w == 0)
        {
            arr[0] = area / w;
            arr[1] = w;
            break;
        }
    }
    return arr;
}