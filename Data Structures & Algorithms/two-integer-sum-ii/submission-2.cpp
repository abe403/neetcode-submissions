class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        unordered_map<int, int> seen;

        vector<int> res;

        for (int i=0; i < numbers.size(); i++) {
            int cur = numbers[i];
            seen[cur] = i;
        }

        for (int i=0; i < numbers.size(); i++) {
            int curnum = numbers[i];

            int offset = target - curnum;

            if (seen[offset]) {
                int num1 = seen[offset];
                num1++;
                
                res.push_back(num1);
                res.push_back(i+1);

                sort(res.begin(), res.end());
                return res;
            }
        }
        return res;
    }
};
