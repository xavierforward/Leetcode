# 41.缺失的第一个正数
## 题目
[原题链接](https://leetcode.com/problems/first-missing-positive/)

## 思路
根据题目使用了计数排序的思路：
- 使用一个新的队列tmps，长度上理论上是传入数组中的最大值；
- 将传入输入的值设置到tmps对应相对应值的下标上；
- 从0开始遍历tmps，返回第一个正整数。

这里只需要返回第一个缺失的正整数，所以对于包含极大整数元素的情况下比较鸡贼的饶了过去，后续再参考大神的解法再做一遍。

## 代码
```java
class Solution {
    public static int firstMissingPositive(int[] nums) {
		List<Integer> tmps = new ArrayList<>(100);
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] > 0 && nums[i] < nums.length+1) {
				while(tmps.size() <= nums[i]+1) {
					tmps.add(null);
				}
				tmps.set(nums[i], 1);
			}
		}
		int res = tmps.size();
		for (int i = 1; i < tmps.size(); i++) {
			if (tmps.get(i) == null) {
				res = i;
				break;
			}
		}
		return res == 0 ? 1 : res;
	}
}
```