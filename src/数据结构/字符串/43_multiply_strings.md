# 43.字符串相乘
## 题目
[原题链接](https://leetcode.com/problems/multiply-strings/)

## 思路

## 代码
```java
class Solution {
    public String multiply(String num1, String num2) {
        int pos[] = new int[num1.length() + num2.length()];
    	for (int i = num1.length()-1; i >= 0; i--) {
    		for (int j = num2.length()-1; j >= 0; j--) {
    			int a = num1.charAt(i) - '0';
    			int b = num2.charAt(j) - '0';
    			int sum = a * b + pos[i+j+1];
    			pos[i+j] += sum / 10;
    			pos[i+j+1] = sum % 10;
    		}
    	}
    	StringBuffer sb = new StringBuffer();
    	for (int p : pos) 
    		if (!(p == 0 && sb.length() == 0)) sb.append(p);
        return sb.length() > 0 ? sb.toString() : "0";
    }
}
```