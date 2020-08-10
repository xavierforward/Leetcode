# 19.删除链表的倒数第N个节点
## 题目
[原题链接](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## 思路
one pass的思路主要在利用两个指针，以n的差距一起移动：
* 创建哑节点，让其next指向head，方便利用next()方法进行统一的判断
* 创建fast节点和slow节点，让其都指向dummy节点
* 让fast节点先移动n+1的位置
* fast节点和slow节点一起移动直至最后
* 删除slow节点的下一个节点
* 返回dummy的下一个节点（即原head）


## 代码
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fastNode = dummy, slowNode = dummy;

        while (n > 0) {
            fastNode = fastNode.next;
            n--;
        }

        while (fastNode.next != null) {
            fastNode = fastNode.next;
            slowNode = slowNode.next;
        }

        slowNode.next = slowNode.next.next;
        return dummy.next;
    }
}
```