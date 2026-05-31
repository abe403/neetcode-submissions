class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        unordered_map<int, int> seen;

        int bignum;
        int lownum;

        for (int i=0; i < numbers.size(); i++) {
            int cur = numbers[i];
            seen[cur] = i;
        }

        for (int i=0; i < numbers.size(); i++) {
            int curnum = numbers[i];

            int offset = target - curnum;

            if (seen.count(offset)) {

                if (seen[offset] != i) {
                    bignum = max((seen[offset])+1, i+1);
                    lownum = min((seen[offset])+1, i+1);

                    return {lownum, bignum};
                }
            }
        }
        return {lownum, bignum};
    }
};
