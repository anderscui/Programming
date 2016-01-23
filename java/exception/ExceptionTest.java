public class ExceptionTest {
	public static void main(String[] args) {
		int[] nums = new int[5];

		try {
			System.out.println("Before exception is generated.");

			nums[5] = 5;
			System.out.println("This won't be displayed.");
		}
		catch (ArrayIndexOutOfBoundsException exc) {
			System.out.println("Index out-of-bounds.");
		}

		System.out.println("After catch statement.");
	}
}
