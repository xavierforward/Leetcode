# 33.搜索旋转排序数组
## 题目
[原题链接](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## 思路
一个二分搜索的变型问题，把握好下一步向左还是向右查询的条件。

## 代码
```java
class Solution {

    public int search(int[] nums, int target) {
        return binarySearch(nums, target, 0, nums.length-1);
    }
    
    public int binarySearch(int[] nums, int target, int start, int end) {
    	if (start > end) {
    		return -1;
    	} else {
    		int mid = (start + end) / 2;
    		if (nums[mid] == target) {
    			return mid;
    		}
    		
    		if (nums[mid] >= nums[start]) {
    			if (target < nums[mid] && target >= nums[start]) {
    				return binarySearch(nums, target, start, mid-1);
    			} else {
    				return binarySearch(nums, target, mid+1, end);
    			}
    		} else if (nums[mid] <= nums[end]){
    			 if (target > nums[mid] && target <= nums[end]) {
    				 return binarySearch(nums, target, mid+1, end);
    			 } else {
    				 return binarySearch(nums, target,  start, mid-1);
    			 }
    		} else {
    			return -1;
    		}
    	}
    }
}
```