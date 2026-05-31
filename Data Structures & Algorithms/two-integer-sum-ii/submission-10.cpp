class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        vector<int> res;

        for (int i=0; i < numbers.size(); i++) {
            for (int j=i+1; j < numbers.size(); j++) {

                if (numbers[i] + numbers[j] == target) {

                    return {min(i+1, j+1), max(i+1, j+1)};
                }
            }
        }
        return {};
    }
};
