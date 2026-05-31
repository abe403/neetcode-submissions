class MinStack {
private:
    stack<int> lowest;
    stack<int> value;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        value.push(val);
        if (lowest.empty()) lowest.push(INT_MAX);
        int low = min(val, lowest.top());
        lowest.push(low);
    }
    
    void pop() {
        if (!value.empty()) {
            value.pop();
            if (!lowest.empty()) lowest.pop();
        }
    }
    
    int top() {
        int top = value.top();
        return top;
    }
    
    int getMin() {
        int minimum;
        if (!lowest.empty()) {
            minimum = lowest.top();
        }
        return minimum;
    }
};

// 5, 3, 7, 0, 2
// 5, 3, 3, 0, 0, 