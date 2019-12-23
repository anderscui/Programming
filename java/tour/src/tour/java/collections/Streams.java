package tour.java.collections;

import tour.java.models.Dish;

import java.io.IOException;
import java.io.PrintStream;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class Streams {
    private static void StreamFromFile() {
        String userDir = System.getProperty("user.dir");
        try (Stream<String> lines = Files.lines(Paths.get(userDir, "src/tour/java/collections/Streams.java"), Charset.defaultCharset())) {
            List<String> words = lines
                    .flatMap(line -> Arrays.stream(line.split("[.\\s]+")))
                    .distinct()
                    .collect(toList());
            System.out.println(words);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void InfiniteStream() {
        Stream<Integer> ns = Stream.iterate(0, n -> n + 2);
        ns.limit(3).forEach(System.out::println);
    }

    public static void main(String[] args) {
        List<Dish> menu = Util.getDishes();
        List<String> highCalDishNames =
                menu.stream()
                        .filter(dish -> dish.getCalories() > 300)
                        .map(Dish::getName)
                        .limit(3)
                        .collect(toList());
        System.out.println(highCalDishNames);

        // flat map
        List<String> names = Arrays.asList("stay hungry", "stay foolish");
        List<String> words =
                names.stream()
                        .map(name -> name.split(" "))
                        .flatMap(Arrays::stream)
                        .distinct().collect(toList());
        System.out.println(words);

        StreamFromFile();
        InfiniteStream();
    }
}
