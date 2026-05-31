class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int size = nums.size();

        if (size == 0) return 0;

        unordered_set<int> seen(nums.begin(), nums.end());

        int best = 0;
        int cur = 1;

        for (auto num : seen) {
            if (!seen.count(num-1)) {
                while (seen.count(num+1)) {
                    cur++;
                    num++;
                }
                best = max(best, cur);
            }
            cur = 1;
        }

        return best;
    }
};
