class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        vector<int> res;

        int big;
        int low;

        for (int i=0; i < numbers.size(); i++) {
            for (int j=0; j < numbers.size(); j++) {
                if (i == j) continue;

                if (numbers[i] + numbers[j] == target) {
                    big = max(i+1, j+1);
                    low = min(i+1, j+1);

                    return {low, big};
                }
            }
        }
        return {low, big};
    }
};
