package tour.java.models;


/**
 * Immutable class.
 */
public class Dish {
    public enum Type { MEAT, FISH, OTHER }

    private final String name;
    private final boolean vegetarian;
    private final int calories;
    private final Type type;

    public Dish(String name, boolean vegetarian, int calories, Type type) {
        this.name = name;
        this.vegetarian = vegetarian;
        this.calories = calories;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public int getCalories() {
        return calories;
    }

    public Type getType() {
        return type;
    }

    public boolean isVegetarian() {
        return vegetarian;
    }
}
