class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> groups;

        vector<vector<string>> res;

        string key;

        for (auto str : strs) {
            key = str;
            sort(key.begin(), key.end());

            groups[key].push_back(str);
        }

        for (auto val : groups) {
            res.push_back(val.second);
        }
        return res;
    }
};
