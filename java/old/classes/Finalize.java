class FDemo {
	int x;

	FDemo(int i) {
		x = i;
	}

	protected void finalize() {
		System.out.println("Finalizing " + x);
	}

	// generates an object that is immediately destroyed.
	void generate(int i) {
		FDemo o = new FDemo(i);
	}
}

public class Finalize {
	public static void main(String[] args) {
		
		FDemo ob = new FDemo(0);
		for (int count = 1; count < 1000000; count++) {
			ob.generate(count);
		}
	}
}
