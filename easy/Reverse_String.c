char* reverseString(char* s) {
    int len = strlen(s);
    char *str = (char*)malloc(sizeof(char) * (len+1));
    for(int i = len-1; i >= 0; i--)
    {
        str[len-1-i] = s[i];
    }
    str[len] = 0;
    return str;
}