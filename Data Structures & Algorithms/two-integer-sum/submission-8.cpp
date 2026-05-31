class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numIndex;

        for (int i = 0; i < nums.size() ; ++i) {
           int complement = target - nums[i];

           auto found = numIndex.find(complement);
           if ( found != numIndex.end() ) {
                return {found->second, i};
           }
           numIndex[nums[i]] = i;
        }
        return {};
    }
};