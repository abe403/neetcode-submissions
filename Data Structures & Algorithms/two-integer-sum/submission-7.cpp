class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_to_index;

        for (int i = 0; i < nums.size() ; ++i) {
           int complement = target - nums[i];

           auto found = num_to_index.find(complement);
           if ( found != num_to_index.end() ) {
                return {found->second, i};
           }
           num_to_index[nums[i]] = i;
        }
        return {};
    }
};