# 10.正则表达式匹配
## 题目
[原题链接](https://leetcode.com/problems/regular-expression-matching/)

## 思路
遍历字符串和正则表达式的字符进行匹配，主要涉及递归和动态分配：
* 创建一个二维数组用于存储每个坐标对应的匹配结果
* 以i,j遍历字符串和正则表达式
* 若i,j对应二维数组有值，则直接返回
* 若j=p的长，则返回i==s的长（最尾部）
* 若p的下一位是*号，则返回跳过*号的返回结果（*为0）或者s下一位字符匹配当前j的结果
* 否则返回当前为的匹配结果&&下一位的匹配结果


## 代码
```java
class Solution {
    public boolean isMatch(String s, String p) {
        Boolean[][] memo = new Boolean[s.length() + 1][p.length() + 1];
        return match(0, 0, s, p, memo) ;
    }

    public boolean match(int i, int j, String s, String p, Boolean[][] memo) {
        if (memo[i][j] != null) {
            return memo[i][j];
        }

        if (j == p.length()) return i == s.length();
        boolean firstMatch = i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.');
        if (j <= p.length() -2 && p.charAt(j+1) == '*') {
            memo[i][j] = match(i, j+2, s, p, memo) || (firstMatch && match(i+1, j, s, p, memo));
        } else {
            memo[i][j] = firstMatch && match(i+1, j+1, s, p, memo);
        }

        return memo[i][j];
    }

}

// 暴力法
class Solution {
    public boolean isMatch(String s, String p) {
         if ("".equals(p)) return "".equals(s);
        boolean firstMatch = !"".equals(s) && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.');
        if (p.length() >= 2 && p.charAt(1) == '*') {
            return isMatch(s, p.substring(2)) || (firstMatch && isMatch(s.substring(1), p));
        } else {
            return firstMatch && isMatch(s.substring(1), p.substring(1));
        }
    }
}

```