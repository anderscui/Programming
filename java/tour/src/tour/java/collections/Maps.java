package tour.java.collections;

import java.util.HashMap;
import java.util.Map;

public class Maps {
    public static void main(String[] args) {
        Map<String, Integer> counts = new HashMap<>();
        counts.put("Alice", 1);
        counts.put("Blue", 2);

        // NullPointer
        int count1 = counts.get("Candy");
        int count2 = counts.getOrDefault("Candy", 0);

        // merge set
        counts.merge("Candy", 1, (a, b) -> a+b);
        System.out.println(counts);

        counts.merge("Candy", 1, (a, b) -> a+b);
        System.out.println(counts);

        counts.forEach((k, v) -> {
            System.out.printf("%s -> %d\n", k, v);
        });

        for (var entry : counts.entrySet()) {
            System.out.printf("%s -> %d\n", entry.getKey(), entry.getValue());
        }

        // new Map interface
        Map<String, Double> capitals = Map.of("Barcelona", 22.5, "New York", 28.3);

        // Use LinkedHashMap to remember the order in which entries were added.
    }
}
