# 50.Pow(x, n)
## 题目
[原题链接](https://leetcode.com/problems/powx-n/)

## 思路
利用[快速幂](https://oi-wiki.org/math/quick-pow/)暴力解，不过没有考虑极限值（n为Integer.MAX_VALUE）。

> 最近也有开始在[paiza](https://paiza.jp/challenges)刷题，感觉起来leetcode在边界值的限制宽松很多。

## 代码
```java
class Solution {
    public double myPow(double x, int n) {
        long N = n;
        return n > 0 ? mySubPow(x, N) : 1/mySubPow(x, -N);
        
    }
    
    private double mySubPow(double x, long n) {
        if (n == 0) {
            return 1.0;
        }
        
        double y = mySubPow(x, n / 2);
        return n % 2 == 0 ? y * y : y * y * x;
    }
}
```