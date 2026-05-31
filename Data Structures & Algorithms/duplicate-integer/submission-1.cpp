class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        std::unordered_map<int, int> numCount;

        for (int i = 0; i < nums.size(); ++i) {
            numCount[nums[i]]++;
            if (numCount[nums[i]] > 1) {
                return true;
            }
        }
        
        return false;
    }
};