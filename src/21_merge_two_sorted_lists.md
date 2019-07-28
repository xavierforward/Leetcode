# 21.合并两个有序链表
## 题目
[原题链接](https://leetcode.com/problems/merge-two-sorted-lists/)

## 思路
### 解法一：
基础的链表解题思路：遍历l1和l2，根据节点值的大小排序到新的链表，直到l1和l2为空

### 解法二：
使用递归，简洁快速

## 代码
```java
// 解法一
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
		ListNode head = null;
		
		while(l1 != null || l2 != null) {
			int next = 0;
			if (l1 != null && l2 != null) {
				if (l2.val > l1.val) {
					next = l1.val;
					l1 = l1.next;
				} else {
					next = l2.val;
					l2 = l2.next;
				}	
			} else if (l1 != null) {
				next = l1.val;
				l1 = l1.next;
			} else {
				next = l2.val;
				l2 = l2.next;
			}
			
			if (head == null) {
				head = new ListNode(next);
				dummy.next = head;
			} else {
				head.next = new ListNode(next);
				head = head.next;
			}
		}
		return dummy.next;
    }
}

// 解法二
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
		if(l2 == null) return l1;
		if(l1.val < l2.val){
			l1.next = mergeTwoLists(l1.next, l2);
			return l1;
		} else{
			l2.next = mergeTwoLists(l1, l2.next);
			return l2;
		}
    }
}
```