# 30.串联所有单词的子串
## 题目
[原题链接](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## 思路
利用双Map，计算一个连续的字符串中匹配字符的命中次数。
**注意：数组的字符长度都相等**

## 代码
```java
class Solution {
    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        if (s.length() == 0 || words.length == 0) {
            return res;
        }

        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        int l = s.length(), wordNum = words.length, wordLength = words[0].length();
        for (int i = 0; i < l - wordNum * wordLength + 1; i++) {
            Map<String, Integer> seenMap = new HashMap<>();
            int j = 0;
            while (j < wordNum) {
                String word = s.substring(i + j * wordLength , i + (j + 1) * wordLength);
                if (wordMap.containsKey(word)) {
                    seenMap.put(word, seenMap.getOrDefault(word, 0) + 1);
                    if (seenMap.get(word) >  wordMap.get(word)) {
                        break;
                    }
                } else {
                    break;
                }
                j ++;
            }
            if (j == wordNum) {
                res.add(i);
            }
        }
        return res;
    }
}
```