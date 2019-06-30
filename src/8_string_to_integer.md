# 8.字符串转换整数 (atoi)
## 题目
[原题链接](https://leetcode.com/problems/string-to-integer-atoi/)

## 思路
* 考虑好各种错误输入情况
* 可以使用正则

## 代码
```java
public class Solution {

    public int myAtoi(String str) {
        if (str == null || "".equals(str) || "".equals(str.trim())) {
            return 0;
        }
        str = str.trim();
        char first = str.charAt(0);
        if (first != '-' && first != '+' && (first > '9' ||  first < '0')) {
            return 0;
        }

        int signed = 1;
        if (first == '-') {
            signed = -1;
            str = str.substring(1, str.length());
        } else if (first == '+') {
            str = str.substring(1, str.length());
        }

        long ans = 0;
        for (int i = 0; i<str.length(); i++) {
            char c = str.charAt(i);
            if (c > '9' ||  c < '0') {
                break;
            }
            ans = ans * 10 + Long.valueOf(c + "");
            if (ans > Integer.MAX_VALUE) {
                ans = Integer.MAX_VALUE;
                if (signed < 0) {
                    ans++;
                }
            }
        }

        return (int)ans* signed;
    }
}

```