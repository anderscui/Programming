interface MyValue {
	double getValue();
}

interface MyParamValue {
	double getValue(double v);
}

public class Lambda {
	public static void main(String[] args) {
		MyValue myVal = () -> 3.14;
		System.out.println("A constant val: " + myVal.getValue());

		MyParamValue myPVal = n -> 1.0/n;
		System.out.println("Reciprocal of 4.0 is " + myPVal.getValue(4.0));
	}
}
