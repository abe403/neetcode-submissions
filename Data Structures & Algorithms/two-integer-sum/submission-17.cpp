class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            seen[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {

            int cur = nums[i];
            int dif = target - cur;

            if (seen.count(dif) && seen[dif] != i ) {
                
                auto [a, b] = minmax(i, seen[dif]);

                return {a, b};
            }
        }
        return {};
    }
};
