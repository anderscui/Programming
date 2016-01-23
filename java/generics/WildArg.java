class BoundTypes<T extends Number> {
	T num;

	BoundTypes(T num) {
		this.num = num;
	}

	double value() {
		return num.doubleValue();
	}

	double reciprocal() {
		return 1 / num.doubleValue();
	}

	double fraction() {
		return num.doubleValue() - num.intValue();
	}

	boolean absEqual(BoundTypes<?> other) {
		return Math.abs(num.doubleValue()) == Math.abs(other.num.doubleValue());
	}
}

public class WildArg {
	public static void main(String[] args) {
		BoundTypes<Double> d = new BoundTypes<Double>(3.0);
		BoundTypes<Float> f = new BoundTypes<Float>(-3.0f);

		System.out.println(f.absEqual(d));
	}
}