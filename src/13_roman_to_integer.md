# 13.罗马数字转整数
## 题目
[原题链接](https://leetcode.com/problems/roman-to-integer/)

## 思路
* 创建两个字典，一个存储单个罗马字符（字典1），一个存储特例罗马字符（字典2）
* 遍历字符串字符
    * 如果当前字符与下一位字符命中字典2，则累加后跳过下一位字符
	* 否则从字典1取值累加

## 代码
```java
class Solution {
    public int romanToInt(String s) {
          Map<Character, Integer> map = new HashMap<Character, Integer>() {{
             put('I', 1);
             put('V', 5);
             put('X', 10);
             put('L', 50);
             put('C', 100);
             put('D', 500);
             put('M', 1000);
        }};
        Map<String, Integer> map2 = new HashMap<String, Integer>() {{
            put("IV", 4);
            put("IX", 9);
            put("XL", 40);
            put("XC", 90);
            put("CD", 400);
            put("CM", 900);
        }};
        int ans = 0;
        for(int i = 0; i < s.length(); i++) {
            if (i+1  <  s.length() && map2.containsKey(s.substring(i, i+2))) {
                ans += map2.get(s.substring(i, i+2));
                i ++;
                continue;
            }
            ans += map.get(s.charAt(i));
        }
        return ans;
    }
}
```