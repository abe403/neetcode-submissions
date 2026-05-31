class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int total = nums.size();

        vector<int> res(total, 1);

        int cur = 1;
        for (int i = 0; i < total; i++) {
            res[i] *= cur;
            cur *= nums[i];
        }
        
        cur = 1;
        for (int i = total-1; i >= 0; i--) {
            res[i] *= cur;
            cur *= nums[i];
        }
        
        return res;
    }
};
