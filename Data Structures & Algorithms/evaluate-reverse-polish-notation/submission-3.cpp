class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;

        int result;

        int a; int b;

        bool postop = false;

        for (int i=0; i < tokens.size(); i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                nums.push(stoi(tokens[i]));
            }
            else {
                    a = nums.top();
                    nums.pop();
                    b = nums.top();
                    nums.pop();
                if (tokens[i] == "+") {
                    result = (b+a);
                }
                else if (tokens[i] == "-") {
                    result = (b-a);
                }
                else if (tokens[i] == "*") {
                    result = (b*a);
                }
                else if (tokens[i] == "/") {
                    result = (b/a);
                }
                nums.push(result);
            }
        }
        return nums.top();
    }
};
