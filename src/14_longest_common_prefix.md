# 14.最长公共前缀
## 题目
[原题链接](https://leetcode.com/problems/longest-common-prefix/)

## 思路
一开始的做法
* 以第一个字符串为基准，遍历所有字符串，判断是否为其子串
* 一旦不为子串，则将基准字符串的最右一位去除

改进做法：遍历次数减少
* 以第一个字符串为基准，遍历所有字符串
* 取基准字符串与当前字符串的最小共通子字符串，更新为基准字符串


## 代码
```java
// 解法1
class Solution {
    public String longestCommonPrefix(String[] strs) {
       if (strs==null || strs.length == 0) return "";
        String ans = strs[0];
        int i = ans.length();
        while(i > -1) {
            for (String str : strs) {
                if (!str.startsWith(ans)) {
                    ans = ans.substring(0, ans.length()-1);
                    break;
                }
            }
            i--;
        }
        return ans;
    }
}

// 解法2
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs==null || strs.length == 0) return "";
        String ans = strs[0];
        int i = 1;
        while(i < strs.length) {
            while (strs[i].indexOf(ans) != 0) {
                ans = ans.substring(0, ans.length()-1);
            }
            i++;
        }
        return ans;
    }
}
```