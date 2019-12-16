public interface Series {

	// all members of an interface are implicitly public.
	int getNext();
	void reset();
	void setStart(int start);

	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}

class ByTwos implements Series {

	int start;
	int val;
	
	ByTwos() {
		start = 0;
		val = 0;
	}

	public int getNext() {
		val += 2;
		return val;
	}

	public void reset() {
		val = start;
	}

	public void setStart(int start) {
		this.start = start;
		val = start;
	}
}

class SeriesTest {
	public static void main(String[] args) {
		ByTwos bt = new ByTwos();
		for (int i = 0; i < 5; i++) {
			System.out.println("Next value is " + bt.getNext());
		}

		System.out.println("Resetting");
		bt.reset();
		for (int i = 0; i < 5; i++) {
			System.out.println("Next value is " + bt.getNext());
		}

		System.out.println("Starting from 100");
		bt.setStart(100);
		for (int i = 0; i < 5; i++) {
			System.out.println("Next value is " + bt.getNext());
		}

		System.out.println("Using interface reference");
		Series s = bt;
		for (int i = 0; i < 5; i++) {
			System.out.println("Next value is " + s.getNext());
		}
	}
}