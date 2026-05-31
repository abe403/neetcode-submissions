class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<int> seen;
        int best = 0;
        int sum = 0;

        int r = 0;
        int l = 0;

        for (r; r<s.size(); r++) {
            while (seen.count(s[r])) {
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[r]);
            best = max(best, r-l+1);
        }
        return best;
    }
};
