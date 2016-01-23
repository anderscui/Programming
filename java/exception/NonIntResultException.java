public class NonIntResultException extends Exception {
	
	int n;
	int d;

	NonIntResultException(int n, int d) {
		this.n = n;
		this.d = d;
	}

	public String toString() {
		return "Result of " + n + " / " + d + " is non-integer.";
	}
}

class CustomExceptionTest {
	public static void main(String[] args) {
		int a = 9;
		int b = 2;

		try {
			if (a % 2 != 0) {
				throw new NonIntResultException(a, b);
			}

			System.out.println(a/b);
		}
		catch (NonIntResultException nire) {
			System.out.println(nire);
		}
	}
}