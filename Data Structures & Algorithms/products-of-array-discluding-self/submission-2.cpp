class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int total = nums.size();

        vector<int> leftProduct(total, 1);
        vector<int> rightProduct(total, 1);

        vector<int> res;

        int cur = 1;
        for (int i = 0; i < total; i++) {
            leftProduct[i] = cur;
            cur *= nums[i];
        }

        cur = 1;
        for (int i = total-1; i > -1; i--) {
            rightProduct[i] = cur;
            cur *= nums[i];
        }

        for (int i=0; i < total; i++) {
            int cur = leftProduct[i] * rightProduct[i];
            res.push_back(cur);
        }
        
        return res;
    }
};
