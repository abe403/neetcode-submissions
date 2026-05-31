class Solution {
public:
    bool isValid(string s) {

        stack<char> p;

        unordered_map<char, char> mp = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (auto& c : s) {
            if (mp.count(c)) {
                if (p.empty()) return false;
                char t = p.top();
                if (t != mp[c]) return false;
                p.pop();
            } else {
                p.push(c);
            }
        }
        if (!p.empty()) return false;
        return true;
    }
};
