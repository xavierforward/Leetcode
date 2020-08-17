# 101.对称二叉树
## 题目
[原题链接](https://leetcode.com/problems/symmetric-tree/)

## 思路
思路同101，不过对称树的条件稍有不同：
1. 两棵树的根节点的值相同
1. 每棵树的左子树与另一棵树的右子树对称
采用递归时条件为：
- 字节点都为空，返回true（当前子树相同）
- 字节点只有一方为空，返回false（当前子树不相同）
- 值不同，返回false（当前子树不相同） 
- 通过的话则进行回调判断：树1的左子树与树2的右子树对称，树1的右子树与树2的左子树点对称

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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isSymmetric(root.left, root.right);
    }

    public boolean isSymmetric(TreeNode left, TreeNode right) {
        if (left == null && right == null)
            return true;
        else if (left == null || right == null)
            return false;
        else if (left.val != right.val) 
            return false;
            
        return isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
    }
}
```
