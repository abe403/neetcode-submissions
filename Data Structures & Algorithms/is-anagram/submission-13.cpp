class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> sc(26, 0);
        vector<int> tc(26, 0);

        for (auto& c : s) {
            int pos = c - 'a';
            sc[pos]++;
        }

        for (auto& c : t) {
            int pos = c - 'a';
            tc[pos]++;
        }

        if (sc != tc) return false;

        return true;
    }
};
