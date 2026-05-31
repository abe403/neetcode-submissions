class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        int length = nums.size();

        std::vector<int> ans;

        ans.resize(2 * length);

        for (int i = 0; i < length; i++) {
            ans[i] = nums[i];
            ans[i+(length)] = nums[i];
        }

        return ans;
    }
};