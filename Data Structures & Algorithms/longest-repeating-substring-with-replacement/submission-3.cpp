class Solution {
public:
    int characterReplacement(string s, int k) {
        int max_len = 0;
        int max_count = 0;
        unordered_map<char, int> mp;
        int left = 0;

        for (int right = 0; right < s.size(); right++) {
            mp[s[right]]++;
            max_count = max(max_count, mp[s[right]]);

            while ((right - left + 1) - max_count > k) {
                mp[s[left]]--;
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};