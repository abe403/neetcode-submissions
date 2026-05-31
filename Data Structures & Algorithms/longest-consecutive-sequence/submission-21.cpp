class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if (nums.size() == 0) return 0;
        
        int best = numeric_limits<int>::min();
        
        int curcount;

        int curnum;

        unordered_set<int> seen(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); i++) {
            curnum = nums[i];
            curcount = 1;

            if (seen.count(curnum - 1)) {
                curcount++;
                while (seen.count(curnum + 1)) {
                    curcount++;
                    curnum++;
                }
            }
            best = max(curcount, best);
        }
        return best;
    }
};
