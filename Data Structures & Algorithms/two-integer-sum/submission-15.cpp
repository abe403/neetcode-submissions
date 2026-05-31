class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size() - 1;

        int sum;
        vector<int> res;

        vector<pair<int, int>> sortednums;

        for (int i=0; i < nums.size(); i++) {
            sortednums.push_back({nums[i], i});
        }

        sort(sortednums.begin(),sortednums.end());

        while (left < right) {
            sum = sortednums[left].first + sortednums[right].first;

            res = {sortednums[left].second, sortednums[right].second};
            sort(res.begin(), res.end());

            if (sum == target) return res;

            else if (sum > target) right--;
            else if (sum < target) left++;
        }
        return {};
    }
};
