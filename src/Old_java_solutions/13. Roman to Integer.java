package Old_java_solutions;

import java.util.*;

class Solution {

    public int romanToInt(String s) {

        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("I", 1);
        hashMap.put("IV", 4);
        hashMap.put("V", 5);
        hashMap.put("IX", 9);
        hashMap.put("X", 10);
        hashMap.put("XL", 40);
        hashMap.put("L", 50);
        hashMap.put("XC", 90);
        hashMap.put("C", 100);
        hashMap.put("CD", 400);
        hashMap.put("D", 500);
        hashMap.put("CM", 900);
        hashMap.put("M", 1000);

        int num = 0;
        String key;
        while (s.length() > 0) {
            if (s.length() == 1) {
                key = s.substring(0, 1);
                System.out.println(key);
                int hmNum = hashMap.get(key);
                num = num + hmNum;
                s = s.substring(1, s.length());
            } else {
                key = s.substring(0, 2);
                System.out.println(key);
                int hmNum;
                try {
                    hmNum = hashMap.get(key);
                    num = num + hmNum;
                    s = s.substring(2, s.length());

                } catch (NullPointerException e) {
                    key = s.substring(0, 1);
                    hmNum = hashMap.get(key);
                    num = num + hmNum;
                    s = s.substring(1, s.length());
                }
            }

        }

        return num;
    }
}
