class Solution {
public:

    string encode(vector<string>& strs) {
        string combined = "";
        for (const auto& str: strs) {
            combined += to_string(str.length()) + "#" + str;
        }
        return combined;
    }
    
    vector<string> decode(string s) {
        // 4#neet4#code4#love4#you
        vector<string> result;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j-i));

            string str = s.substr(j+1, length);
            result.push_back(str);

            i = j + 1 + length;
        }
        return result;
    }
};
