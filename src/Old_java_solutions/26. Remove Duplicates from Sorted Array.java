package Old_java_solutions;

class Solution {
    public int removeDuplicates(int[] nums) {

        int indexToChange = 0;

        for (int i = 1; i < nums.length; i++) {

            if (nums[i] > nums[indexToChange]) {
                indexToChange++;
                nums[indexToChange] = nums[i];
            }
        }
        return indexToChange + 1;
    }
}