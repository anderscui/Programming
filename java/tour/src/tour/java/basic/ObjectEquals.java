package tour.java.basic;

import java.util.HashSet;

public class ObjectEquals {
    private int x;
    private int y;
    private int z;

    public ObjectEquals(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        ObjectEquals other = (ObjectEquals) o;
        return x == other.x && y == other.y && z == other.z;
    }

    @Override
    public int hashCode() {
        var result = 17;
        result = 31 * result + x;
        result = 31 * result + y;
        result = 31 * result + z;
        return result;
    }

    public String toString() {
        return String.format("object: (%d, %d, %d)", x, y, z);
    }

    public static void main(String[] args) {
        var o1 = new ObjectEquals(1, 2, 3);
        var o2 = new ObjectEquals(1, 2, 2);

        assert !o1.equals(o2);
        assert !o1.equals("other object");

        HashSet<ObjectEquals> set1 = new HashSet<>();
        set1.add(o1);
        System.out.println(o1.hashCode());
        System.out.println(set1.size());

        System.out.println(o1);
    }
}
