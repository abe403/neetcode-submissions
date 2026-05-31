class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> numcount;
        
        for (auto num : nums) {
            numcount[num]++;
        }

        vector<pair<int, int>> countvector;

        for (auto p : numcount) {
            countvector.push_back(p);
        }

        sort(countvector.begin(), countvector.end(), [](auto& a, auto& b) {
            return a.second > b.second;
        });

        vector<int> result;

        for (int i=0; i<k; i++) {
            result.push_back(countvector[i].first);
        }
        return result;
    }
};
