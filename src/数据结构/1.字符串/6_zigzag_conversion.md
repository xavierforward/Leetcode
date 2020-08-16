# 6.Z字形变换
## 题目
[原题链接](https://leetcode.com/problems/zigzag-conversion/)

## 思路
* 使用String数组记录每一行的非空字符
* 使用行坐标和列坐标迭代字符串，列坐标递增，行坐标在0到numRows之间移动
* 按照行坐标和列坐标将字符写入对应的String数组
* 迭代String数组，汇总成一行返回
* 特殊情况：numRows为1

## 代码
```java
public class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1)
            return s;

        char[] chars = s.toCharArray();
        int rowIndex = 0;
        int carry = 1;
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i<chars.length; i++) {
            if (rows[rowIndex] == null) {
                rows[rowIndex] = new StringBuilder();
            }
            rows[rowIndex].append(chars[i]);
            rowIndex += carry;
            if (rowIndex == 0) {
                carry = 1;
            } else if (rowIndex == numRows-1) {
                carry = -1;
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < rows.length; i++) {
            if (rows[i] != null)
                ans.append(rows[i]);
        }

		return ans.toString();
    }
}
```