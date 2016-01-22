class Outer {
	int[] nums;

	Outer(int[] n) {
		nums = n;
	}

	void analyze() {
		Inner inner = new Inner();
		System.out.println("Minimum: " + inner.min());
		System.out.println("Maximum: " + inner.max());
		System.out.println("Average: " + inner.avg());
	}

	class Inner {
		int min() {
			int m = nums[0];
			for (int i = 1; i < nums.length; i++) {
				if (nums[i] < m) {
					m = nums[i];
				}
			}
			return m;
		}

		int max() {
			int m = nums[0];
			for (int i = 1; i < nums.length; i++) {
				if (nums[i] > m) {
					m = nums[i];
				}
			}
			return m;
		}

		double avg() {
			int sum = 0;
			for (int i: nums) {
				sum += i;
			}
			return 1.0 * sum / nums.length;
		}
	}
}

public class NestedClass {
	public static void main(String[] args) {

		int[] a = { 3, 2, 1, 5, 6, 9, 7, 8 };
		Outer outer = new Outer(a);
		outer.analyze();
	}
}
