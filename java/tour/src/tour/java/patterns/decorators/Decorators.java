package tour.java.patterns.decorators;

public class Decorators {
    public static void main(String[] args) {
        ChristmasTree tree = new Garland(new ChristmasTreeImpl());
        System.out.println(tree.decorate());

        ChristmasTree tree2 = new BubbleLights(new Garland(new Garland(new ChristmasTreeImpl())));
        System.out.println(tree2.decorate());
    }
}
