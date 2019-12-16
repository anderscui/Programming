public class CatchOrder {
	public static void main(String[] args) {
		int[] numbers = { 4, 8, 16, 32, 64 };
		int[] denoms = { 2, 0, 8 };

		for (int i = 0; i < numbers.length; i++) {
			try {
				System.out.println(numbers[i] + " / " + denoms[i] + " is " + numbers[i] / denoms[i]);
			}
			catch (ArrayIndexOutOfBoundsException ex) {
				System.out.println("No matching element found.");
			}
			catch (Throwable th) {
				System.out.println("Some excetion occurred.");
			}
		}
	}
}
