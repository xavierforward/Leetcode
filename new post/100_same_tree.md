# 100.相同的树
## 题目
[原题链接](https://leetcode.com/problems/same-tree/)

## 思路
递归判断，返回条件：
- 字节点都为空，返回true（当前子树相同）
- 字节点只有一方为空，返回false（当前子树不相同）
- 值不同，返回false（当前子树不相同）
通过的话则分别对左右子树是否相同进行回掉判断。

## 代码
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;
        else if (p == null || q == null)
            return false;
        else if (p.val != q.val)
            return false;
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```
