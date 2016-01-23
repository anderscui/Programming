public class Uncaught {
	public static void main(String[] args) {
		int[] nums = new int[5];

		System.out.println("Before exception is generated.");
		nums[5] = 5;
		System.out.println("This won't be displayed.");
	}
}
