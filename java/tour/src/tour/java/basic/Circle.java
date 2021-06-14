package tour.java.basic;

import tour.java.patterns.decorators.ChristmasTree;

import java.util.HashSet;

// a class example
public class Circle implements Comparable<Circle> {
    public static double PI = 3.1415;

    protected final int x, y, r;

    // basic ctor
    public Circle(int x, int y, int r) {
        checkRadius(r);

        this.x = x;
        this.y = y;
        this.r = r;
    }

    // copy ctor
    public Circle(Circle original) {
        x = original.x;
        y = original.y;
        r = original.r;
    }

    // getters
    public int getX() { return x; }
    public int getY() { return y; }
    public int getR() { return r; }

    protected void checkRadius(double radius) {
        if (radius < 0.0) {
            throw new IllegalArgumentException("radius may not < 0");
        }
    }

    @Override
    public String toString() {
        return String.format("center=(%d, %d); radius=%d", x, y, r);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        // covers o is null
        if (!(o instanceof Circle)) {
            return false;
        }

        var other = (Circle)o;
        return x == other.x && y == other.y && r == other.r;
    }

    @Override
    public int hashCode() {
        var result = 17;
        result = 31 * result + x;
        result = 31 * result + y;
        result = 31 * result + r;
        return result;
    }

    @Override
    public int compareTo(Circle other) {
        long result = (long) other.y - this.y;
        if (result == 0) result = (long) this.x - other.x;
        if (result == 0) result = (long) this.r - other.r;

        return Long.signum(result);
    }

    // static methods
    public static double area(double r) { return PI * r * r; }

    public static void main(String[] args) {
        var c1 = new Circle(0, 0, 1);
        var c2 = new Circle(1, 1, 1);
        var c3 = new Circle(c1);
        System.out.println(c1 + " <> " + c2 + " <> " + c3);
        System.out.println("area of c1: " + Circle.area(c1.r));

        var s1 = new HashSet<Circle>();
        s1.add(c1);
        s1.add(c2);
        s1.add(c3);
        System.out.println(s1.size() + " elements: " + s1);
    }
}
