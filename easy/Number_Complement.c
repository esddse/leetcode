int findComplement(int num) {
    int i;
    for(i = 31; i >= 0; i--)
        if( (num >> i) & 1 == 1)
            break;
    
    return (1 << (i+1)) - num - 1;
}