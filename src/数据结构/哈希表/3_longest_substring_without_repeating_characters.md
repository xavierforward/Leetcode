# 3.无重复字符的最长子串
## 题目
[原题链接](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 思路
这道题我一开始采用的是暴力法，虽然可以通过但运行效率很慢，这里记录下官方Solution的优化滑动窗口的思路：

* 创建一个哈系表用于存储字符index
* 初始化左右坐标跟踪位i，j为0
* 以j为索引遍历字符：
	* 若字符已经存在于哈系表中，更新i为max(新字符的index，i)，这里考虑了新字符与最右边字符相同的情况
	* 更新新字符index为j+1，存入哈系表
	* 更新最长长度等于max(最长长度, j+1-i)

## 代码
### 暴力法
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        String re = "";
        for (int i = 0; i < s.length(); i++) {
            StringBuilder sub = new StringBuilder();
            sub.append(s.charAt(i));
            for (int j = i + 1; j < s.length(); j++) {
                if (sub.indexOf(s.charAt(j) + "") > -1) {
                    break;
                } else {
                    sub.append(s.charAt(j));
                }
            }

            if (sub.length() > re.length()) {
                re = sub.toString();
            }

        }
        return re.length();
    }
}
```

### 优化滑动窗口解法
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int result = 0;
        for (int i = 0, j = 0; j < s.length(); j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            map.put(s.charAt(j), j + 1);
            result = Math.max(result, j - i + 1);
        }
        return result;
    }
}
```
