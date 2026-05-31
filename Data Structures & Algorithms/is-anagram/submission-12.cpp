class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char, int> freq;

        for (auto& c : s) {
            freq[c]++;
        }

        for (auto& c: t) {
            freq[c]--;
        }

        for (auto& [k, v] : freq) {
            if (v != 0) return false;
        }

        return true;
    }
};
