package tour.java.basic;

public class varArgs {

    private static double average(double... values) {
        double sum = 0;
        for (double v: values) {
            sum += v;
        }
        return values.length == 0 ? 0 : sum/values.length;
    }

    public static void main(String[] args) {
        // natural way
        System.out.println(average(1, 2, 3, 4, 5));

        // explicit array
        double[] scores = { 3, 4, 5, 6, 7};
        System.out.println(average(scores));

        // empty inputs
        System.out.println(average());
    }
}
