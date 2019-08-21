# 27.移除元素
## 题目
[原题链接](https://leetcode.com/problems/remove-element/)

## 思路
- 根据提示将解题思路转化为将数组中不等于指定参数的数移动到数组最前面

## 代码
```java
class Solution {
    public int removeElement(int[] nums, int val) {
       if (nums.length == 0) return 0; 
    	int i = 0;
    	for (int j = 0; j < nums.length; j++) {
    		if (nums[j] != val) {
    			nums[i] = nums[j];
    			i++;
    		}
    	}
		return i;
    }
}
```