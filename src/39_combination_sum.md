# 39.组合总和
## 题目
[原题链接](https://leetcode.com/problems/combination-sum/)

## 思路
考察遍历的题目，我的思路是从左到右来构建返回的数组直到和等于target：
- 遍历排序后的数组，查找target和遍历值的商数
- 遍历商数，依次创建从1个到商数个的当前遍历值的数组
- 用目标值减去上面数组的和，得到新target，一次作为参数遍历
- 直到新target为0返回

在评论区学到了解法2，也是用递归，比较不同的在于他是每次先用遍历数字填充满后再移除，代码简洁很多。

## 代码
### 解法1
```java
class Solution {
    	public List<List<Integer>> combinationSum(int[] candidates, int target) {
    	List<List<Integer>>  res = new ArrayList<>();
    	Arrays.sort(candidates);
    	res.addAll(combinationSumSub(new ArrayList<>(), candidates, target, 0));
    	return res;
    }
    
    public List<List<Integer>> combinationSumSub(List<Integer> prefixList, int[] candidates, int target, int start) {
    	List<List<Integer>>  res = new ArrayList<>();
    	for (int i = start; i < candidates.length; i++) {
    		int candidate = candidates[i];
    		int sum = target / candidate;
    		while (sum != 0) {
    			int target2 = target - candidate * sum;
    			if (target2 == 0) {
    				res.add(createList(prefixList, candidate, sum));
    			} else if (i < candidates.length-1 && target2 >= candidates[i+1]) {
    				res.addAll(combinationSumSub(createList(prefixList, candidate, sum), candidates, target2, i+1));
    			}
    			sum--;
    		}
    	}
    	return res;
    }
    
    private List<Integer> createList(List<Integer> prefixs, int num, int times) {
    	List<Integer> res = new ArrayList<>();
		for (Integer pre : prefixs) {
			res.add(pre);
		}
    	while (times > 0) {
    		res.add(num);
    		times--;
    	}
    	return res;
    }
}
```

### 解法2
```java
public List<List<Integer>> combinationSum(int[] nums, int target) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, target, 0);
    return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
    if(remain < 0) return;
    else if(remain == 0) list.add(new ArrayList<>(tempList));
    else{ 
        for(int i = start; i < nums.length; i++){
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i); // not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1);
        }
    }
}
```