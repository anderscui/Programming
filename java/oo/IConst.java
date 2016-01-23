interface IConst {
	int MIN = 0;
	int MAX = 10;
	String ERRORMSG = "Boundary Error";
}

class IConstD implements IConst {
	public static void main(String[] args) {
		int[] nums = new int[MAX];
		for (int i = MIN; i < MAX; i++) {
			nums[i] = i;
			System.out.print(nums[i] + " ");
		}
		System.out.println();
	}
}