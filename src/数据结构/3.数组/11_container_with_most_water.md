# 11.盛最多水的容器
## 题目
[原题链接](https://leetcode.com/problems/container-with-most-water/)

## 思路
使用双指针法，分别从第一个数和最后一个数开始遍历，
因为面积取决于最小的高，所以获取面积后，高较小的一边的指针向中间移动。

## 代码
```java
class Solution {
    public int maxArea(int[] height) {
        int i = 0, j = height.length -1, maxArea = 0;

        while (j > i) {
            int x = j  - i;
            int y = Math.min(height[i], height[j]);
            maxArea = maxArea < x*y ? x*y : maxArea;

            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        return maxArea;
    }
}
```