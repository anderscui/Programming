public class ThrowableInfo {
	public static void getException() {
		int[] numbers = { 4, 8, 16, 32, 64 };
		int[] denoms = { 2, 0, 8 };

		for (int i = 0; i < numbers.length; i++) {
			try {
				System.out.println(numbers[i] + " / " + denoms[i] + " is " + numbers[i] / denoms[i]);
			}
			catch (ArithmeticException ex) {
				System.out.println("Can't divide by zero.");
			}
			catch (ArrayIndexOutOfBoundsException ex) {
				System.out.println("No matching element found.");
				throw ex;
			}
		}
	}

	public static void main(String[] args) {
		try {
			Rethrow.getException();
		}
		catch (ArrayIndexOutOfBoundsException ex) {
			System.out.println("Standard message is: ");
			System.out.println(ex);
			System.out.println("\nStack trace: ");
			ex.printStackTrace();

			System.out.println("Fatal error - program terminated");
		}
	}
}