class Solution {
public:
    void reverse_c_str(char* start, char* end)
    {
        char temp;
        while (start <= end - 1)
        {
            temp = *start;
            *start = *end;
            *end = temp;
            start++;
            end--;
        }
    };

    string reverseWords(string s) {
        if (s.size() == 0) {
            return string();
        }
        char* c_string= (char *) s.c_str();
        char* temp = c_string;
        char* start = c_string;
        while (true)
        {
            while (*temp != '\0' && *temp != ' ')
                temp++;
            this->reverse_c_str(start, temp - 1);
            if (*temp == '\0')
                break;
            start = ++temp;
        }
        return string(c_string);
    };
};
