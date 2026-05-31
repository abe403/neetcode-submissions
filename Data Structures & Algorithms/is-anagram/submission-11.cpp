class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char, int> schar;
        unordered_map<char,int> tchar;

        for (auto& c : s) {
            schar[c]++;
        }

        for (auto& c: t) {
            tchar[c]++;
        }

        for (auto& [k, v] : schar) {
            if (auto it = tchar.find(k); it == tchar.end()) return false;
            if (v != tchar[k]) return false;
        }

        for (auto& [k, v] : tchar) {
            if (auto it = schar.find(k); it == schar.end()) return false;
            if (v != schar[k]) return false;
        }

        return true;
    }
};
