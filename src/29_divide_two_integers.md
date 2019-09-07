# 29.两数相除
## 题目
[原题链接](https://leetcode.com/problems/divide-two-integers/)

## 思路
主要思路计算除数可以减多少次被除数，因为一次一次减效率低，每次减被除数的倍数（用位运算替代），直到除数小于被除数，有几个需要注意的点：
- Math.abs(x) 函数对于x等于Integer.MIN_VALUE时，会返回Integer.MIN_VALUE本身；
- Integer.MIN_VALUE减1等于Integer.MAX_VALUE


## 代码
```java
class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        boolean isNeg = (dividend < 0) ^ (divisor < 0);
        dividend = Math.abs(dividend);
        divisor = Math.abs(divisor);
        int res = 0, i = 0;
        while (dividend - divisor >= 0) {
            for (i = 0; dividend - (divisor << i << 1) >= 0; i++);
            res += 1 << i;
            dividend -= divisor << i;
        }
        return isNeg ? -res : res;
    }
}
```