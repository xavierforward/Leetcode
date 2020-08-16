# 35.搜索插入位置
## 题目
[原题链接](https://leetcode.com/problems/search-insert-position/)

## 思路
稍微修改下标准二分查找就可以解了，
不过在解答区看到的一个解法（解法二）感觉更有助于理解二分查找，
思路就是二分查找匹配到则返回匹配的下标，没有则在最后返回最新的左下标。

## 代码
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int res = 0;
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
        	int mid = (left + right) / 2;
        	if (nums[mid] < target && (mid == nums.length - 1 || nums[mid+1] >= target)) {
        		res = mid + 1;
        	}
        	
        	if (nums[mid] < target) {
        		left = mid + 1;
        	} else {
        		right = mid - 1;
        	}
        }
		return res;
    }
}

// 解法二
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length-1;
        while(left<=right){
            int mid = (left + right) / 2;
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
}
```