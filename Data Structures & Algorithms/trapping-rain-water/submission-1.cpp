class Solution {
public:
    int trap(vector<int>& height) {

        int prefix;
        int suffix;

        int watlvl = 0;

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
