public class Varargs {

	static void vaTest(String msg, int ... v) {
		System.out.println(msg + v.length);
		System.out.println("Contents: ");

		for (int i = 0; i < v.length; i++) {
			System.out.println(" arg " + i + ": " + v[i]);
		}
		System.out.println();
	}

	public static void main(String[] args) {
		vaTest("One Varargs: ", 10);
		vaTest("Three Varargs: ", 1, 2, 3);
		vaTest("No Varargs: ");
	}
}
