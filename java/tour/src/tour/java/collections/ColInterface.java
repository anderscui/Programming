package tour.java.collections;

import java.util.*;

public class ColInterface {
    public static void main(String[] args) {
        Collection<String> c = new HashSet<>();
        Collection<String> d = Arrays.asList("one", "two");
        Collection<String> e = Collections.singleton("only one");

        // add elements
        c.add("zero");
        c.addAll(d);

        // copy a collection
        Collection<String> copy = new ArrayList<>(c);

        // query size
        System.out.println("is empty? " + c.isEmpty());
        System.out.println("c size: " + c.size());

        // contains
        System.out.println("contains zero? " + c.contains("zero"));
        System.out.println("contains d collection? " + c.containsAll(d));

        // `copy` to array
        var elements = c.toArray();
        var strElements = c.toArray(new String[0]);

        c.remove("zero");
        c.removeAll(e);
        c.retainAll(d);
        System.out.println(c);
        c.clear();
    }
}
