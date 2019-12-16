public abstract class Shape2D {

    private double width;
    private double height;
    private String kind;

    Shape2D(double w, double h, String k) {
        width = w;
        height = h;
        kind = k;
    }

    // accessors
    double getWidth() { return width; }
    double getHeight() { return height; }
    void setWidth(double w) { width = w; }
    void setHeight(double h) { height = h; }
    String getKind() { return kind; }

    void showDim() {
        System.out.println("Width and height are " + width + " and " + height);
    }

    abstract double area();
}

class Triangle extends Shape2D {
    private String style;

    Triangle(double w, double h, String s) {
        // super must be the first statement executed inside a subclass constructor.
        super(w, h, "triangle");

        style = s;
    }

    // override area() of Shape2D.
    double area() {
        return getWidth() * getHeight() / 2;
    }

    void showStyle() {
        System.out.println("Triangle is " + style);
    }
}

class ColorTriangle extends Triangle {
    private String color;

    ColorTriangle(double w, double h, String s, String c) {
        super(w, h, s);

        color = c;
    }

    String getColor() { return color; }

    void showColor() {
        System.out.println("Color is " + color);
    }
}

class Rectangle extends Shape2D {
    Rectangle(double w, double h) {
        super(w, h, "rectangle");
    }

    boolean isSquare() {
        return getWidth() == getHeight();
    }

    double area() {
        return getWidth() * getHeight();
    }
}

class Shapes {
    public static void main(String[] args) {
        Triangle t1 = new Triangle(4.0, 4.0, "filled");
        Triangle t2 = new Triangle(8.0, 12.0, "outlined");

        System.out.println("Info for t1: ");
        t1.showStyle();
        t1.showDim();
        System.out.println("Area is " + t1.area());

        System.out.println();

        System.out.println("Info for t2: ");
        t2.showStyle();
        t2.showDim();
        System.out.println("Area is " + t2.area());

        System.out.println();

        ColorTriangle t3 = new ColorTriangle(8.0, 12.0, "outlined", "blue");
        System.out.println("Info for t3: ");
        t3.showStyle();
        t3.showDim();
        t3.showColor();
        System.out.println("Area is " + t3.area());

        System.out.println();
        // Abstract class
        Shape2D[] shapes = new Shape2D[3];
        shapes[0] = t1;
        shapes[1] = new Rectangle(10, 5);
        shapes[2] = t3;

        for (Shape2D shape: shapes) {
            System.out.println("object is " + shape.getKind());
            System.out.println("area is " + shape.area());
            System.out.println();
        }
    }
}
