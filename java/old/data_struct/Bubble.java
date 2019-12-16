// Loops an array
public class Bubble {

	static void bubble(int arr[], int n) {
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < n - i; j++) {
				if (arr[j] > arr[j+1]) {
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		}
	}

	public static void main(String[] args) {
		//int nums[] = new int[10];
		int nums[] = { 99, -10, 100123, 18, -978, 5623, 463, -9, 287, 49 };
		bubble(nums, 10);

		for (int i = 0; i < 10; i++) {
			System.out.print(nums[i] + " ");
		}
		System.out.println();
	}
}
