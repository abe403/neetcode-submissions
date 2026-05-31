#include <array>

class Solution {
public:
    struct ArrayHash {
        size_t operator()(const array<int, 26>& a) const {
            size_t h = 0;
            for (int x : a) {
                h = h * 31 + x;
            }
            return h;
        }
    };
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<array<int, 26>, vector<string>, ArrayHash> mp;

        vector<vector<string>> res;

        for (auto& str: strs) {
            array<int, 26> freq{};
            for (auto& c : str) {
                int key = c - 'a';
                freq[key]++;
            }
            mp[freq].push_back(str);
        }

        for (auto& val : mp) {
            res.push_back(val.second);
        }
        return res;
    }
};