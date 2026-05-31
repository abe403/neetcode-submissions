class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int highest;

        int maximum  = 0;

        for (int i=0; i<prices.size(); i++) {
            for (int j=i+1; j<prices.size(); j++) {

                int difference = prices[j] - prices[i];
                maximum = max(difference, maximum);
            }
        }
        return maximum;
    }
};
