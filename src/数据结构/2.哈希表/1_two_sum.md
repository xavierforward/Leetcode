---
title: 1.两数之和
author: 西泽
date: 2020-08-10 20:00:00
tags:
    - 哈希表
---

# 1.两数之和
## 题目
[原题链接](https://leetcode.com/problems/two-sum/)

## 思路
使用哈系表提高效率

## 代码
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int key = target - nums[i];
            if (map.containsKey(key)) {
                return new int[]{ map.get(key), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("没有符合的结果");
    }
}
```
