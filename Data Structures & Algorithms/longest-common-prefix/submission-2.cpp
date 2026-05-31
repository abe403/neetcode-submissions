class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        std::string res = "";

        for (int i = 0; i < strs[0].size(); ++i) {
            char c = strs[0][i];

            std::cout << c << std::endl;

            for (int j = 1; j < strs.size(); ++j) {
                if (strs[j][i] != strs[0][i]) {
                    return res;
                }
            }
            res += c;
        }
        return res;
    }
};