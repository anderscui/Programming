public class Queue {

	char[] items;
	int putloc, getloc;

	Queue(int size) {
		items = new char[size];
		putloc = getloc = 0;
	}

	// copy data from another queue
	Queue(Queue other) {
		putloc = other.putloc;
		getloc = other.getloc;

		items = new char[other.items.length];
		for (int i = getloc; i < putloc; i++) {
			items[i] = other.items[i];
		}
	}

	// construct with init values
	Queue(char a[]) {

		items = new char[a.length];
		putloc = getloc = 0;

		for (char c: a) {
			put(c);
		}
	}

	void put(char item) {
		if (putloc == items.length) {
			System.out.println(" - Queue is full.");
			return;
		}

		items[putloc++] = item;
	}

	char get() {
		if (getloc == putloc) {
			System.out.println(" - Queue is empty.");
			return (char)0;
		}

		return items[getloc++];
	}
}

class QueueTest {

	static void showQueue(Queue q) {
		char c;
		do {
			c = q.get();
			System.out.print(c + " ");
		} while(c != (char)0);

		System.out.println();
	}

	public static void main(String[] args) {

		Queue q1 = new Queue(10);
		// put some chars into q1
		for (int i = 0; i < 10; i++) {
			q1.put((char)('A' + i));
		}

		// init values
		char[] name = { 'T', 'o', 'm' };
		Queue q2 = new Queue(name);

		// copy
		Queue q3 = new Queue(q1);

		showQueue(q1);
		showQueue(q2);
		showQueue(q3);

		System.out.println();
	}
}
