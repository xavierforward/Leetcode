# 2.两数相加
## 题目
[原题链接](https://leetcode.com/problems/add-two-numbers/)

## 思路
* 初始化头节点并作为当前节点
* 设置进位值为0
* 循环参数节点直至都不再有下一位节点
	* 两个节点的值和进位值相加
	* 根据相加值是否大于10重新设置进位值，并生成下一位节点
	* 将当前节点指向下一位节点
	* 将参数节点指向各自的下一位节点
* 如果还有进位值，则以进位值生成下一位子节点
* 返回头节点的下一位节点

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode header = new ListNode(0);
        ListNode curr = header;
        int carry = 0;

        while (l1 != null || l2 != null) {
            int x = l1 != null ? l1.val : 0;
            int y = l2 != null ? l2.val : 0;
            int z = x + y + carry;
            carry = z / 10;
            curr.next = new ListNode(z % 10);
            curr = curr.next;
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }

        if (carry > 0) {
            curr.next = new ListNode(carry);
        }

        return header.next;
    }
}
```