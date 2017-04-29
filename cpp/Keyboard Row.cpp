class Solution {
public:
    bool word_in_line(string word, string line) {
        for(char letter : word) {
            letter = letter >= 'A' and letter <= 'Z' ? letter + ('a' - 'A'): letter;
            if (line.find(letter) == string::npos) {
                return false;
            }
        }
        return true;
    }

    vector<string> findWords(vector<string>& words) {
        string line_1 = string("qwertyuiop");
        string line_2 = string("asdfghjkl");
        string line_3 = string("zxcvbnm");
        vector<string> result;
        for(string word : words) {
            if (this->word_in_line(word, line_1) || this->word_in_line(word, line_2) || this->word_in_line(word, line_3)) {
                result.push_back(word);
            }
        }
        return result;
    }
};
