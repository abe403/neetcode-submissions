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
                best = max(best, (int)seen.size());
            } else {
                best = max(best, (int)seen.size());
                l++;
                r = l;
                seen.clear();
            }

        }
        return best;
    }
};
