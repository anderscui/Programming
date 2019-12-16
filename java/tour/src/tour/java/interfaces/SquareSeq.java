package tour.java.interfaces;

public class SquareSeq implements IntSequence {
    private int i;

    @Override
    public boolean hasNext() {
        return true;
    }

    @Override
    public int next() {
        i++;
        return i*i;
    }
}
