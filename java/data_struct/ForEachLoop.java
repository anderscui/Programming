public class ForEachLoop {
	public static void main(String[] args) {
		
		int[] nums = { 1, 2, 3, 4, 5 };

		int sum = 0;
		for (int i: nums) {
			sum += i;
		}

		System.out.println(sum);

		int[] numbers = { 6, 8, 3, 7, 5, 6, 1, 4 };
		int key = 5;
		boolean found = false;

		for(int i: numbers) {
			if (i == key) {
				found = true;
				break;
			}
		}

		if (found) {
			System.out.println("Value found:)");
		} else {
			System.out.println("Value not found:(");
		}
	}
}
