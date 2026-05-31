class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = INT_MAX;
        int best = 0;
        for (int i=0; i<prices.size(); i++) {
            lowest = min(lowest, prices[i]);
            best = max(best, prices[i] - lowest);
        }
        return best;
    }
};
