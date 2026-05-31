class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int size = nums.size();

        if (size == 0) return 0;

        unordered_set<int> seen(nums.begin(), nums.end());

        int best = 0;
        int cur = 1;

        for (auto num : seen) {
            int curnum = num;
            if (!seen.count(curnum-1)) {
                while (seen.count(curnum+1)) {
                    cur++;
                    curnum++;
                }
                best = max(best, cur);
            }
            cur = 1;
        }

        return best;
    }
};
