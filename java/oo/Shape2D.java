public class Shape2D {

    double width;
    double height;

    void showDim() {
        System.out.println("Width and height are " + width + " and " + height);
    }
}

class Triangle extends Shape2D {
    String style;

    Triangle(double w, double h, String style) {
        width = w;
        height = h;
        this.style = style;
    }

    double area() {
        return width * height / 2;
    }

    void showStyle() {
        System.out.println("Triangle is " + style);
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
    }
}
