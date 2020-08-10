# 23.合并K个排序链表
## 题目
[原题链接](https://leetcode.com/problems/merge-k-sorted-lists/)

## 思路
思路跟21题相同，查找的地方应该可以进行优化

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
    public ListNode mergeKLists(ListNode[] lists) {
        
        Integer minVal = null, minIdx = null;

        for (int i = 0; i < lists.length; i++) {
            ListNode node = lists[i];
            if (node == null) continue;
            if (minVal == null || minVal > node.val) {
                minVal = node.val;
                minIdx = i;
            }
        }

        if (minVal == null) {
            return null;
        }

        ListNode res = lists[minIdx];
        lists[minIdx] = lists[minIdx].next;
        res.next = mergeKLists(lists);
        return res;
    }
}
```