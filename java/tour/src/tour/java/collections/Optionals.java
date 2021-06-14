package tour.java.collections;

import java.util.Optional;

public class Optionals {
    public static void main(String[] args) {
        Optional<String> os = Optional.empty();
        System.out.println(os.orElse("default value"));
        System.out.println(os.orElseGet(() -> "default value"));
        // var strVal = os.orElseThrow(IllegalStateException::new);

        // if present
        os = Optional.of("new value");
        os.ifPresent(System.out::println);
        os.ifPresentOrElse(System.out::println, () -> System.out.println("without value"));
    }
}
