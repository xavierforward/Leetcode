# 48.旋转图像
## 题目
[原题链接](https://leetcode.com/problems/rotate-image/)

## 思路
简单粗暴的解法，从最外面的矩形的四角开始顺时针方向转动。  
关键数值（假设矩形长n）：
- 总共有n/2个正方形需要转动；
- 一个正方形需要转动正方形边长-1次（n-2*t-1，t为当前正方形圈数）；

## 代码
```java
class Solution {
    public static void rotate(int[][] matrix) {
    	rotateOneCircle(0, matrix);
    }
    
    public static void rotateOneCircle(int t, int[][] matrix) {
        int n = matrix.length;

    	if (t >= n/2) {
    		return;
    	}
    	
    	int changeCount = n - 2 * t -1; 
    	
    	// one circle rotate
        for (int i = 0; i < changeCount; i++) {
        	// one circle change 4 value
        	// clockwise
        	int tmp = matrix[t][t + i];
        	matrix[t][t + i] = matrix[n - 1 - t -i][t];
        	matrix[n - 1 - t -i][t] = matrix[n - 1 - t][n - 1 - t - i];
        	matrix[n - 1 - t][n - 1 - t - i] = matrix[t+i][n - 1 - t];
        	matrix[t+i][n - 1 - t] = tmp;
        }
        
        // rotate next circle
        rotateOneCircle(t+1, matrix);
    }
}

```



