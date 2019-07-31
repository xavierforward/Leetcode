# 7.整数反转
## 题目
[原题链接](https://leetcode.com/problems/reverse-integer/)

## 思路
* 使用long计算防止溢出
* 遍历x直到为0，每次遍历将x最左边一位放到ans最左边
* 若ans超出Integer范围则返回0

## 代码
```java
public class Solution {

    public int reverse(int x) {
        long ans = 0;

        while(x != 0) {
            ans = ans*10+x % 10;
            x = x/10;
        }

        if (ans < Integer.MIN_VALUE || ans > Integer.MAX_VALUE) {
            return 0;
        } else {
            return (int)ans;
        }
    }

}

```