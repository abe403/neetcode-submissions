class Solution {
public:
    int trap(vector<int>& height) {
        // int l = 0;
        // int r = heights.size() - 1;

        int prefix = 0;
        int suffix = 0;

        int watlvl = 0;

        vector<int> levels(height.size());

        for (int i = 0; i < height.size(); i++) {
            prefix = 0;
            suffix = 0;

            for (int l = 0; l < i; l++) {
                prefix = max(height[l], prefix);
            }
            for (int r = height.size() - 1; r > i; r--) {
                suffix = max(height[r], suffix);
            }

            int curlvl = min(prefix, suffix) - height[i];
            curlvl = max(0, curlvl);
            watlvl += curlvl;
        }
        return watlvl;
    }
};
