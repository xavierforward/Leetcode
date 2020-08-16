# 28.实现strStr()
## 题目
[原题链接](https://leetcode.com/problems/implement-strstr/)

## 思路
这道题应该是要考KMP算法的，不过完全忘了，先用暴力法解了，后续再补充KMP算法的解法。

## 代码
```java
class Solution {
    public int strStr(String haystack, String needle) {
		  int i = 0, j = 0;
		    while (i < haystack.length() && j < needle.length()) {
		    	if (haystack.charAt(i) == needle.charAt(j)) {
		    		i++;
		    		j++;
		    	} else {
		    		i = i - j + 1;
		    		j = 0;
		    	}
		    }
			return j == needle.length() ? i - j : -1; 
    }
}
```