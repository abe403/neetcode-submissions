class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int best = 0;

        int l = 0;
        int r = 0;
        
        unordered_set<char> seen;

        while (r < s.size()) {

            if (seen.insert(s[r]).second) {
                r++;
            } else {
                seen.erase(s[l]);
                l++;
            }
            best = max(best, (int)seen.size());
        }
        return best;
    }
};
