interface GenTest<T> {
	boolean test(T n, T m);
}

public class GenInterface {
	public static void main(String[] args) {
		GenTest<Integer> isFactor = (n, m) -> (n % m) == 0;
		if (isFactor.test(10, 2)) {
			System.out.println("2 is a factor of 10");
		}
		System.out.println();

		GenTest<String> isIn = (a, b) -> a.indexOf(b) >= 0;
		String hello = "Hello World";
		if (isIn.test(hello, "Hello")) {
			System.out.println("'Hello' is found");
		}
	}
}
