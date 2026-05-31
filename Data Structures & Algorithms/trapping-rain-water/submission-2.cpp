class Solution {
public:
    int trap(vector<int>& height) {
        
        int n = height.size();

        int prefix = 0;
        int suffix = 0;

        vector<int> maxLeft(n);
        vector<int> maxRight(n);

        for (int l = 0; l < n; l++) {
            maxLeft[l] = prefix;
            prefix = max(prefix, height[l]);
        }

        for (int r = n-1; r >= 0; r--) {
            maxRight[r] = suffix;
            suffix = max(suffix, height[r]);
        }

        int watlvl = 0;

        for (int i = 0; i < n; i++) {
            
            int lowestside = min(maxLeft[i], maxRight[i]);
            int curlvl = lowestside - height[i];
            curlvl = max(0, curlvl);
            watlvl += curlvl;
        }
        return watlvl;
    }
};
