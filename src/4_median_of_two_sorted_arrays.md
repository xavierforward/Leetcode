# 4.寻找两个有序数组的中位数
## 题目
[原题链接](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## 思路
利用中位数的定义解题

## 代码
```java
class Solution {
    public double findMedianSortedArrays(int[] a, int[] b) {
        int m = a.length;
        int n = b.length;
        if (m > n) {
            int[] tmpNums = a; a = b; b = tmpNums;
            int tmp = m; m= n; n = tmp;
        }

        int iMin = 0, iMax = m, half = (m + n +1) / 2;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = half - i;

            if (i < iMax && b[j-1] > a[i]) {
                iMin = i + 1;
            } else if (i > iMin && a[i-1] > b[j]) {
                iMax = i - 1;
            } else {
                int left = 0;
                if (i == 0)
                    left = b[j-1];
                else if (j == 0)
                    left = a[i-1];
                else
                    left = Math.max(a[i-1], b[j-1]);
                if ((m+n) % 2 == 1)
                    return left;

                int right = 0;
                if (i == m)
                    right = b[j];
                else if (j == n)
                    right = a[i];
                else
                    right = Math.min(a[i], b[j]);
                return (left + right) / 2d;
            }
        }
        return 0d;
    }
}
```