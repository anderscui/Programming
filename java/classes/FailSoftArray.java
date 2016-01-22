public class FailSoftArray {
	private int a[];
	private int errVal;
	public int length;

	public FailSoftArray(int size, int errv) {
		this.a = new int[size];
		this.errVal = errv;
		this.length = size;
	}

	public int get(int index) {
		if (indexOK(index)) {
			return a[index];
		}
		return errVal;
	}

	public boolean put(int index, int val) {
		if (indexOK(index)) {
			a[index] = val;
			return true;
		}
		return false;
	}

	public boolean indexOK(int index) {
		return (index >= 0 && index < length);
	}
}

class FSDemo {
	public static void main(String[] args) {

		FailSoftArray fsa = new FailSoftArray(5, -1);

		int x;
		System.out.println("Fail quietly");
		for (int i = 0; i < (fsa.length * 2); i++) {
			fsa.put(i, i*10);
		}

		for (int i = 0; i < (fsa.length * 2); i++) {
			x = fsa.get(i);
			if (x != -1) {
				System.out.print(x + " ");
			}
		}
		System.out.println();
	}
}
