package tour.java.collections;

import java.util.HashSet;
import java.util.Set;

public class Sets {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>(Util.getNames());
        set.forEach(System.out::println);
    }
}
