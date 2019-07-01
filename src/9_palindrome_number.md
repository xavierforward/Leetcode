# 9.Palindrome Number
## 题目
[原题链接](https://leetcode.com/problems/palindrome-number/)

## 思路
这道题可以使用字符串反转后是否相等来做，不过我用类似第七题int反转的方法：

* 处理特殊值：负数各位正数，0为结尾的数字
* 初始化y，遍历x，将x的个位数依次反转后赋予y，在y大于x之前，如果出现x与y相等的情况，则为回数
* 第二步需要考虑x长度为奇数和偶数的情况

## 代码
```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        } else if (-1 < x  && x < 10) {
            return true;
        } else if (x%10 == 0){
            return false;
        }

        int y = 0;
        while (x > y) {
            int tmp = x%10;
            x = x/10;

            if (x == y) {
                return true;
            }

            y = y*10 + tmp;

            if (x == y) {
                return true;
            }
        }

        return false;
    }
}
```