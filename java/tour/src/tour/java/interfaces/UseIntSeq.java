package tour.java.interfaces;

public class UseIntSeq {
    private static double average(IntSequence seq, int n) {
        int count = 0;
        double sum = 0;
        while (seq.hasNext() && count < n) {
            sum += seq.next();
            count++;
        }
        return count == 0 ? 0 : sum/count;
    }

    public static void main(String[] args) {
        IntSequence squares = new SquareSeq();
        double avg = average(squares, 100);
        System.out.println(avg);
    }
}
