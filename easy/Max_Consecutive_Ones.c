int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int maxLen = 0;
    int cnt = 0;
    bool inSeq = false;
    for(int i = 0; i < numsSize; i++)
    {
        if(nums[i] == 1)
        {
            if(!inSeq)
            {
                inSeq = true;
                cnt ++;   
            }
            else
            {
                cnt++;
            }
        }
        else
        {
            if(inSeq)
            {
                inSeq = false;
                if(cnt > maxLen)
                    maxLen = cnt;
                cnt = 0;
            }
        }
        
    }
    
    if(cnt > maxLen)
        maxLen = cnt;
    return maxLen;
}