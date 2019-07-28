# 17.电话号码的字母组合
## 题目
[原题链接](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## 思路
* 创建返回字符串列表
* 遍历输入数字，字符串列表作为参数
	* 创建新的字符串列表
	* 根据字符串列表参数和数字对应的字符，创建新的字符串，加入新创建的字符串列表
	* 返回新的字符串列表，作为下一次遍历的参数
	
## 代码
```java
class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<>();
        if (digits == null ||"".equals(digits)) return ans;
        Map<Integer, String> map = new HashMap() {{
            this.put(0, "abc");
            this.put(1, "def");
            this.put(2, "ghi");
            this.put(3, "jkl");
            this.put(4, "mno");
            this.put(5, "pqrs");
            this.put(6, "tuv");
            this.put(7, "wxyz");
        }};
        ans.add("");
        for (char numer : digits.toCharArray()) {
            ans = expand(ans, map.get(numer - '2'));
        }
        return ans;
    }

    public List<String> expand(List<String> last, String letters) {
        List<String> next = new ArrayList<>();
        for (char c : letters.toCharArray()) {
            for (String res : last) {
                next.add(res + c);
            }
        }
        return next;
    }
}
```