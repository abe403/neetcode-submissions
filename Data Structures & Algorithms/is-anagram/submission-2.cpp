class Solution {
public:
    bool isAnagram(string s, string t) {

        std::unordered_map<int, int> sCount;

        std::unordered_map<int, int> tCount;

        size_t length;

        if (s.size() != t.size()) {
            return false;
        } else {
            length = s.size();
        }

        for (size_t i = 0; i < length; ++i) {
            char charS = s.at(i);
            sCount[charS]++;
        }

        for (size_t i = 0; i < length; ++i) {
            char charT = t.at(i);
            
            tCount[charT]++;

            if (tCount[charT] > sCount[charT] ) {
                return false;
            }
        }
        return true;        
    }
};
