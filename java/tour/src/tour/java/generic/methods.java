package tour.java.generic;

import java.io.PrintStream;
import java.lang.reflect.Array;
import java.util.Arrays;

public class methods {
    private static <T> void swap(T[] array, int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] args) {
        Integer[] intArray = {1, 2, 3};
        methods.swap(intArray, 0, 1);
        System.out.println(Arrays.toString(intArray));

        String[] strArray = {"a", "b", "c"};
        methods.swap(strArray, 0, 1);
        System.out.println(Arrays.toString(strArray));
    }
}
