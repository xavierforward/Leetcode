# 24.两两交换链表中的节点
## 题目
[原题链接](https://leetcode.com/problems/swap-nodes-in-pairs/)

## 思路
题目规定一定要有节点交换，不过写得出值交换的解法也差不多，后续只需要将交换值改为交换节点即可。
用递归也可以。

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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy1 = new ListNode(0);  // 用来返回的节点
        ListNode dummy2 = new ListNode(0);  // 指向进行交换的两个节点的前一个节点
        dummy1.next = head;
        dummy2.next = dummy1;

        while(head != null && head.next != null) {
            
            ListNode tmp = head.next; 
            head.next = head.next.next;
            tmp.next = head;
            dummy2.next.next = tmp;

            dummy2.next = head;
            head = head.next;
        }
        return dummy1.next;
    }
}

// 递归
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode next = head.next;
        head.next = swapPairs(next.next);
        next.next = head;
        return next;
    }
}

```