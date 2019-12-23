package tour.java.collections;

import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;

public class Iterations {
    public static void main(String[] args) {
        // forEach for collections
        Collection<String> names = Arrays.asList("anders", "bill", "candy");
        names.forEach(System.out::println);

        // foreach
        for (String name: names) {
            System.out.println(name);
        }

        // iterators
        Iterator<String> iterator = names.iterator();
        while (iterator.hasNext()) {
            String val = iterator.next();
            System.out.println(val);
        }
    }
}
