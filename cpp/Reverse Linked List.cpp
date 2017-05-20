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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode *start = head;
        ListNode * temp = head->next;
        ListNode * prev = NULL;

        start->next = NULL;
        while (temp->next) {
            prev = head;
            head = temp;
            temp = temp->next;
            head->next = prev;
        }
        temp->next = head;
        return temp;
    }
};
