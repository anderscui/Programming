package tour.java.patterns.decorators;

public class Garland extends TreeDecorator {
    public Garland(ChristmasTree tree) {
        super(tree);
    }

    @Override
    public String decorate() {
        return super.decorate() + " with " + decorateWithBubbleLights();
    }

    private String decorateWithBubbleLights() {
        return "Garland";
    }
}
