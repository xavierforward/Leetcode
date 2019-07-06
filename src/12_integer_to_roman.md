# 12.整数转罗马数字
## 题目
[原题链接](https://leetcode.com/problems/integer-to-roman/)

## 思路
* 按规律从大到小除以数字得到余数（代表对应罗马数字字符应该出现的次数）
* 根据余数拼接对应的罗马数字字符

## 代码
```java
class Solution {
    public String intToRoman(int num) {
        int[] bases = new int[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romaChars = new String[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder re = new StringBuilder();
        for (int i = 0; i< bases.length; i++) {
            int j = num / bases[i];
            if (j == 0) continue;
            for (int k = j; k > 0; k--) {
                re.append(romaChars[i]);
            }
            num -= j * bases[i];
            if (num == 0) break;
        }
        return re.toString();
    }
}
```