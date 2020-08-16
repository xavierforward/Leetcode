# 32.最长有效括号
## 题目
[原题链接](https://leetcode.com/problems/longest-valid-parentheses/)

## 思路
- 括号问题一般使用栈
- 初始时将`-1`入栈，记录为最左下标
- 左括号入栈，右括号出栈
- 出栈后，如果栈为空，更新最左下标
- 出栈后，如果栈不为空，判断本次出战后的有效括号长度，如果更长则更新
- **促发更新返回值的点应该是出栈后栈不为空，因为连续右括号是一直出栈的**

## 代码
```java
class Solution {
    public int longestValidParentheses(String s) {
		int res = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    res = Math.max(res, i - stack.peek());
                }
            }
        }
        return res;
    }
}
```