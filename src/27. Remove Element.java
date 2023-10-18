class Solution {

    public static int removeElement(int[] nums, int val) {

        int numberOfOffenders = 0;
        int indexToMove = nums.length - 1;

        for (int i = 0; i < nums.length; i++) {

            if (i == indexToMove) {
                return nums.length - numberOfOffenders;

            }

            if (indexToMove != 0) {
                while (nums[indexToMove] == val) {
                    indexToMove--;
                }
            }

            if (nums[i] == val) {
                int temp = nums[i];
                nums[i] = nums[indexToMove];
                nums[indexToMove] = temp;
                numberOfOffenders++;
            }
        }
        return nums.length - numberOfOffenders;
    }
}