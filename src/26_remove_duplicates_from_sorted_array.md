# 26.删除排序数组中的重复项
## 题目
[原题链接](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## 思路
- 根据提示将解题思路转化为将数组不重复的数移动到数组最前面
- 使用双指针

## 代码
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
    	int i = 0;
    	for (int j = 1; j < nums.length; j++) {
    		if (nums[i] != nums[j]) {
    			nums[i+1] = nums[j];
    			i++;
    		}
    	}
    	return i+1;
    }
}
```