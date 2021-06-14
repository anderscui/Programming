package tour.java.patterns.decorators;

public class BubbleLights extends TreeDecorator {
    public BubbleLights(ChristmasTree tree) {
        super(tree);
    }

    @Override
    public String decorate() {
        return super.decorate() + " with " + decorateWithBubbleLights();
    }

    private String decorateWithBubbleLights() {
        return "Bubble Lights";
    }
}
