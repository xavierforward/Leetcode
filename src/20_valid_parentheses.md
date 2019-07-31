# 20.有效的括号
## 题目
[原题链接](https://leetcode.com/problems/valid-parentheses/)

## 思路
利用堆的后进先出特性进行解题：
* 创建堆对象和字典
* 遍历字符串
    * 如果字符是左括号，则放进堆中
    * 如果字符是右括号，则检查最后放进堆的元素（堆为空则直接返回false），是匹配的括号则从堆中移除
* 遍历完成后如果堆为空则返回true

## 代码
```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        List<Character> openBrackets = Arrays.asList('(', '[' ,'{');
        List<Character> closeBrackets = Arrays.asList(')', ']' ,'}');

        for (Character c : s.toCharArray()) {
            if (openBrackets.contains(c)) {
                stack.push(c);
            } else if (closeBrackets.contains(c)) {
                if (!stack.isEmpty()) {
                    Character lastBracket = stack.peek();
                    if (closeBrackets.indexOf(c) == openBrackets.indexOf(lastBracket)) {
                        stack.pop();
                    } else {
                        break;
                    }
                } else {
                    return false;
                }
            }

        }
        return stack.isEmpty();
    }
}
```