import java.util.HashMap;

class Solution {
    
    public int[] twoSum(int[] nums, int target) {
      //  int[] targetNumbers = new int[2];
       HashMap<Integer, Integer> numMap = new HashMap<>();

       for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // If the complement is in the HashMap, return the indices
            if (numMap.containsKey(complement)) {
                return new int[] {numMap.get(complement), i};
            }
            // Put the current number and its index into the HashMap
            numMap.put(nums[i], i);
        }
        return null;
    }
}