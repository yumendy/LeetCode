/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) {
            return l2;
        } else if (!l2) {
            return l1;
        } else {
            ListNode * a = l1;
            ListNode * b = l2;
            ListNode * result = NULL;
            ListNode * last = NULL;

            while (true) {
                while (a && a->val < b->val) {
                    if (!result) {
                        result = last = a;
                        a = a->next;
                    } else {
                        last->next = a;
                        last = last->next;
                        a = a->next;
                        if (!a) {
                            break;
                        }
                    }
                }
                if (!a) {
                    last->next = b;
                    break;
                }
                while (b && a->val >= b->val) {
                    if (!result) {
                        result = last = b;
                        b = b->next;
                    } else {
                        last->next = b;
                        last = last->next;
                        b = b->next;
                        if (!b) {
                            break;
                        }
                    }
                }
                if (!b) {
                    last->next = a;
                    break;
                }
            }
            return result;
        }
    }
};
