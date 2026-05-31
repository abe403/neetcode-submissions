class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> result_map;

        for (auto word : strs) {
            string key = word;
            sort(key.begin(), key.end());
            result_map[key].push_back(word);
        }

        vector<vector<string>> result_vector;

        for (auto pair : result_map) {
            result_vector.push_back(pair.second);
        }
        return result_vector;
    }
};
