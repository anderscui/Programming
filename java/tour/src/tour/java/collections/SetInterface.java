package tour.java.collections;

import java.util.Arrays;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

public class SetInterface {
    public static void main(String[] args) {
        SortedSet<String> s = new TreeSet<>(Arrays.asList("book", "animal", "count"));
        for (var word : s) {
            // elements are sorted
            System.out.println(word);
        }
        var firstElem = s.first();
        var lastElem = s.last();

        // weird.
        var tailSet = s.tailSet(firstElem + '\0');
        System.out.println(tailSet);

        Set<String> s2 = Set.of("Hello", "World");
    }
}
