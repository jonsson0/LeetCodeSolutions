import java.util.Arrays;

class Solution {

    public static String longestCommonPrefix(String[] strs) {

        Arrays.sort(strs);

        String first = strs[0];

        String last = strs[strs.length - 1];

        StringBuilder sBuilder = new StringBuilder();

        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) == last.charAt(i)) {
                sBuilder.append(first.charAt(i));
            } else {
                return sBuilder.toString();
            }
        }
        return sBuilder.toString();

    }
}