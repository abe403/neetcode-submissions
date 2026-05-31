class Solution {
public:
    bool isAnagram(string s, string t) {

        std::unordered_map<int, int> sCount;

        std::unordered_map<int, int> tCount;

        if (s.size() != t.size()) {
            return false;
        }

        for (int i = 0; i < s.size(); ++i) {
            char charS = s.at(i);
            sCount[charS]++;
        }

        for (int i = 0; i < t.size(); ++i) {
            char charT = t.at(i);
            
            tCount[charT]++;

            if (tCount[charT] > sCount[charT] ) {
                return false;
            }
        }
        return true;        
    }
};
