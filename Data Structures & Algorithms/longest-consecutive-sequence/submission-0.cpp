class Solution {
public:
    int longestConsecutive(const std::vector<int>& nums) {
        if ( nums.empty() ) {
            return 0;
        }

        unordered_set<int> num_set(nums.begin(), nums.end());

        int max_length = 0;

        for (int num : num_set) {
            int current_num = num;
            int current_length = 1;
            
            if ( num_set.find(current_num - 1) == num_set.end()) {
                
                while (num_set.find(current_num + 1) != num_set.end()) {
                    current_length++;
                    current_num++;
                }
                max_length = max(max_length, current_length);
            }
        }
        return max_length;
    }
};
