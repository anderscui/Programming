package tour.java.collections;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayLists {
    private final static int INIT = 2, GROW_FACTOR = 2;

    private static void expandArray() {
        int[] nums = new int[INIT];
        int next = 0;
        for (int i = 0; i < 20; i++) {
            if (next >= nums.length) {
                int[] tmp = new int[nums.length * GROW_FACTOR];
                System.arraycopy(nums, 0, tmp, 0, nums.length);
                System.out.println(String.format("%d -> %d", nums.length, tmp.length));
                nums = tmp;
            }
            nums[next++] = i;
        }
    }

    private static void useArrayList() {
        ArrayList<Integer> nums = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            nums.add(i);
        }
        System.out.println(nums.get(0));

        List<String> names = Arrays.asList("anders", "bill", "candy");
        names.forEach(System.out::println);
    }

    public static void main(String[] args) {
        // expandArray();
        useArrayList();
    }
}
