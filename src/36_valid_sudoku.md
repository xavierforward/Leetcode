# 36.有效的数独
## 题目
[原题链接](https://leetcode.com/problems/valid-sudoku/)

## 思路
分别验证当前数在其行，列，块上没有重复值，只要想出来块的下标计算方法就可以了。

## 代码
```java
class Solution {
   public boolean isValidSudoku(char[][] board) {
    	List<ArrayList<Character>> rows = new ArrayList<ArrayList<Character>>();
    	List<ArrayList<Character>> columns = new ArrayList<ArrayList<Character>>();
    	List<ArrayList<Character>> blocks = new ArrayList<ArrayList<Character>>();
    	for (int i = 0; i < 9; i++) {
    		rows.add(new ArrayList<Character>());
    		columns.add(new ArrayList<Character>());
    		blocks.add(new ArrayList<Character>());
    	}
    	for (int i = 0; i < board.length; i++) {
    		for (int j = 0; j < board[i].length; j++) {
    			char n = board[i][j];
    			if ('.' != n) {
    				int blockIndex = i / 3 + j / 3 * 3;
    				if (rows.get(i).contains(n) || columns.get(j).contains(n) || blocks.get(blockIndex).contains(n)) {
    					return false;
    				} else {
    					rows.get(i).add(n);
    					columns.get(j).add(n);
    					blocks.get(blockIndex).add(n);
    				}
    			}
    		}
    	}
    	return true;
    }
}

```