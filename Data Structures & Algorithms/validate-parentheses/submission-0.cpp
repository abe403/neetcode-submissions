class Solution {
public:
    bool isValid(string s) {
        stack<char> p;
        set<char> op = {'(', '[','{'};
        set<char> cl = {')', ']', '}'};
        for (auto& c : s) {
            if ( c == '(' || c == '[' || c == '{') {
                p.push(c);
            }
            if ( c == ')' || c == ']' || c == '}') {
                if (p.empty()) return false;
                char t = p.top();
                if (c == ')' && t != '(') return false; 
                else if (c == ']' && t != '[') return false; 
                else if (c == '}' && t != '{') return false;
                p.pop();
            }
        }

        if (!p.empty()) return false;

        return true;
    }
};
