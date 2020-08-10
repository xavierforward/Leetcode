# 5.最长回文子串
## 题目
[原题链接](https://leetcode.com/problems/longest-palindromic-substring/)

## 思路
* 使用回文定义，按条件计算

## 代码
```java
public class Solution {

    public String longestPalindrome(String s) {

        char[] arr = s.toCharArray();
        String re = "";

        for (int i = 0; i < arr.length; i++) {
            int begin = 0, end = 0;

            int j = 1;
            while (i - j + 1 > 0 && i + j < arr.length && arr[i - j] == arr[i + j]) {
                j++;
            }
            if (2 * j - 1 > re.length()) {
                begin = i - j + 1;
                end = i + j;
            }

            if (i + 1 < arr.length && arr[i] == arr[i + 1]) {
                j = 1;
                while (i - j + 1 > 0 && i + j + 1 < arr.length && arr[i - j] == arr[i + j + 1]) {
                    j++;
                }
                if (2 * j > re.length() && 2 * j > end - begin) {
                    begin = i - j + 1;
                    end = i + j + 1;
                }
            }

            if (end - begin > 0) {
                re = s.substring(begin, end);
            }
        }
        return re;
    }

}

```