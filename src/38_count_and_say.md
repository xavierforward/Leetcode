# 38.报数
## 题目
[原题链接](https://leetcode.com/problems/count-and-say/)

## 思路
- 根据上一个结果推导当前结果
- 推导时，计算当前字符`c`连续重复次数`n`（最小为1），追加`nc`到结果字符串

## 代码
```java
class Solution {
    public String countAndSay(int n) {
       String res = "1";
        for (int i = 1; i < n; i++) {
        	StringBuilder sb = new StringBuilder();
        	char pre = res.charAt(0);
        	int count = 1;
        	for (int j = 1; j < res.length(); j++) {
        		char cur = res.charAt(j);
        		if (pre == cur) {
        			count++;
        		} else {
        			sb.append(count).append(pre);
        			count = 1;
        			pre = cur;
        		}
        	}
        	sb.append(count).append(pre);
        	res = sb.toString(); 
        }
    	return res;
    }
}
```