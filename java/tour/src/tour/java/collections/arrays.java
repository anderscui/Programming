package tour.java.collections;

import java.util.Arrays;
import java.util.Comparator;

public class arrays {
    public static void main(String[] args) {
        int[] primes = { 2, 3, 5, 7, 17, 31, 11 };
        Arrays.sort(primes);
        for (int prime : primes) {
            System.out.println(prime);
        }

        // a trailing comma
        String[] authors = {
                "James Gosling",
                "Guy Steele",
                "Bill Joy",
        };
        Arrays.sort(authors, Comparator.comparing(s -> s.substring(1)));
        System.out.println(Arrays.toString(authors));
    }
}
