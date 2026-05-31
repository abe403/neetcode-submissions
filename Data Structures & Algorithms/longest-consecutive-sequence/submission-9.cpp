class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int length = nums.size();

        if (length == 0) {
            return 0;
        }

        int best = 1;

        sort(nums.begin(), nums.end());

        int cur = 1;

        for (int i=0; i < length - 1; i++) {
            if ( nums[i+1] == nums[i]) {
                continue;
            }

            if ( (nums[i+1] - nums[i]) == 1 ) {
                cur++;
                best = max(best, cur);
            } else {
                cur = 1;
            }
        }
        return best;
    }
};
