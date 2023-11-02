package Old_java_solutions;

class Solution {
    public ListNode mergeTwoLists(ListNode node1, ListNode node2) {

        ListNode currNode = new ListNode(0);
        ListNode firstNode = new ListNode();


        while (node1 != null && node2 != null) {

            if (node1.val < node2.val) {
                if (currNode.val == 0) {
                    firstNode = node1;
                }
                currNode.next = node1;
                currNode = currNode.next;
                node1 = node1.next;
            } else {
                if (currNode.val == 0) {
                    firstNode = node2;
                }
                currNode.next = node2;
                currNode = currNode.next;
                node2 = node2.next;
            }
        }

        if (node1 != null) {
            currNode.next = node1;
        }
        if (node2 != null) {
            currNode.next = node2;
        }
        if (currNode.val == 0) {
            return new ListNode();
        }
        return firstNode;
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}