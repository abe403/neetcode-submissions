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
                
                vector<int> res = {i, seen[dif]};

                sort(res.begin(), res.end());

                return res;
            }
        }
        return {};
    }
};
