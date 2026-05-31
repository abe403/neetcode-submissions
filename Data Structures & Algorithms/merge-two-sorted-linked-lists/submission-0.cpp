/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode* cur = list1;

        vector<int> res;

        while (cur != nullptr) {
            res.push_back(cur->val);
            cur = cur->next;
        }

        cur = list2;

        while (cur != nullptr) {
            res.push_back(cur->val);
            cur = cur->next;
        }

        sort(res.begin(), res.end());

        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;

        for (auto x : res) {
            tail->next = new ListNode(x);
            tail = tail->next;
        }

        return dummy->next;

    }
};
