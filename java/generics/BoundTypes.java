public class BoundTypes<T extends Number> {
	T num;

	BoundTypes(T num) {
		this.num = num;
	}

	double reciprocal() {
		return 1 / num.doubleValue();
	}

	double fraction() {
		return num.doubleValue() - num.intValue();
	}
}

class BoundTypesTest {
	public static void main(String[] args) {
		BoundTypes<Integer> i = new BoundTypes<Integer>(5);
		System.out.println("Reciprocal: " + i.reciprocal() + " fraction: " + i.fraction());

		BoundTypes<Double> d = new BoundTypes<Double>(3.14);
		System.out.println("Reciprocal: " + d.reciprocal() + " fraction: " + d.fraction());		
	}
}