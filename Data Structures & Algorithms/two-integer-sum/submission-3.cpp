class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        std::unordered_map<int, int> count;
        std::vector<int> result;

        for ( int i = 0; i < nums.size() ; ++i ) {
           int difference = target - nums[i];

           auto it = count.find(difference);

           if ( it != count.end() ) {
                result.push_back(count[difference]);
                result.push_back(i);

                std::sort(result.begin(), result.end());

                return result;
           } else {
            count[nums[i]] = i;
           }
        }
        return {};
    }
};