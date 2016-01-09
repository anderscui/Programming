import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Vocabulary v = new ListVocabulary(new ArrayList<String>());
        v.add("Java");
        v.add("Java8");
        v.add("Python");
        v.add("Pythonic");
        v.add("C");
        v.add("C#");
        v.add("C++");

        System.out.println(v.isPrefix("J"));
        System.out.println(v.isPrefix("Java"));
        System.out.println(v.isPrefix("Java6"));

        /////

        Vocabulary v2 = new ListVocabulary(new ArrayList<String>());
        v2.add("Java");
        v2.add("Java8");
        v2.add("Python");
        v2.add("Pythonic");
        v2.add("C");
        v2.add("C#");
        v2.add("C++");

        System.out.println(v2.isPrefix("J"));
        System.out.println(v2.isPrefix("Java"));
        System.out.println(v2.isPrefix("Java6"));
    }
}
