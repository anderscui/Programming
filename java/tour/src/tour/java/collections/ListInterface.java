package tour.java.collections;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListInterface {
    public static void main(String[] args) {
        List<String> l = new ArrayList<String>(Arrays.asList("book", "animal", "comedy"));
        List<String> words = Arrays.asList("hello", "world");
        List<String> words2 = List.of("hello", "world");

        String first = l.get(0);
        String last = l.get(l.size() - 1);
        System.out.println("l: " + l);

        // update value
        l.set(0, last);
        System.out.println("l: " + l);

        // append
        l.add(first);
        // prepend
        l.add(0, first);
        System.out.println("l: " + l);

        // sub list as a view
        List<String> sub = l.subList(1, 3);
        sub.set(0, "hi");
        System.out.println("l: " + l);

        var i = l.indexOf(first);
        System.out.println(i);
        i = l.indexOf(first + first);
        // -1 for not found
        System.out.println(i);


    }
}
