# 16.最接近的三数之和
## 题目
[原题链接](https://leetcode.com/problems/3sum-closest/)

## 思路
这道题的实现基本跟3Sum同一个思路，不过在细节在有些差别，主要是边界判断从是否相等变成是否大于或小于：

* 按从小到大将数组排列
* 遍历数组，依次固定最左边值，创建left，right指向后续值的最左和最右的坐标
* 判断坐标i，left，right指向的三数之和和target的大小：
	* 相等直接返回
	* 三数之和小于target，left加1，并且对left后续的数进行判断去重
	* 三数之和大于target，right减1，并且对right后续的数进行判断去重
	* 判断三数之和是否更加接近target，是的话更新结果值

## 代码
```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int numClosest = nums[0] + nums[1] + nums[nums.length-1];
        for(int i = 0; i < nums.length-2; i++) {
            int left = i + 1, right = nums.length - 1;
            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    left++;
                    while (left+1 < right && nums[i] + nums[left+1] + nums[right] < target)  left++;
                } else {
                    right--;
                    while (left < right-1 && nums[i] + nums[left] + nums[right-1] > target)  right--;
                }

                if (Math.abs(sum - target) < Math.abs(numClosest - target)) {
                    numClosest = sum;
                }
            }
        }
        return numClosest;
    }
}
```