# 31.下一个排列
## 题目
[原题链接](https://leetcode.com/problems/next-permutation/)

## 思路
- 确定一个最大索引`i`保证`i`的右边是一个降序序列，即`nums[i] >= nums[i+1]`，没有则翻转数组；
- 从`i`的右边确定另一个索引`j`，使`nums[i] > nums[j]`；
- 替换`i`和`j`对应的值；
- 将`i`右边的降序序列改成升序序列。

## 代码
```java
class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i+1] <= nums[i]) {
            i--;
        }

        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }

        reverse(nums, i+1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

}
```