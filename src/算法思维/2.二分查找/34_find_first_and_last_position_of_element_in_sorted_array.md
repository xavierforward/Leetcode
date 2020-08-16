# 34.在排序数组中查找元素的第一个和最后一个位置
## 题目
[原题链接](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## 思路
二分查找应用题
- 查找最左边的元素nums[left]
- 如果nums[left]的下一位是相同值，则再调用一次二分查找找出最右边元素nums[right]

## 代码
```java
class Solution {
	public int[] searchRange(int[] nums, int target) {
		int[] res = {-1, -1};
		int left = searchExtreme(nums, target, true);
		if (left == -1) {
			return res;
		} else {
			if (left == nums.length-1 || (left < nums.length-1 && nums[left+1] != target)) {
				res[0] = left;
				res[1] = left;
				return res;
			} else {
				int right = searchExtreme(nums, target, false);
				res[0] = left;
				res[1] = right;
				return res;
			}
		}
    }
	
	public int searchExtreme(int[] nums, int target, boolean searchLeft) {
		int res = -1;
		int min = 0;
		int max = nums.length-1;
		while (min <= max) {
			int mid = (min + max) / 2;
			if (nums[mid] == target) {
				res = mid;
				if (searchLeft) {
					max = mid - 1;
				} else {
					min = mid + 1;
				}
			} else if (nums[mid] > target) {
				max = mid - 1;
			} else {
				min = mid + 1;
			}
		}
		return res;
	}
}
```