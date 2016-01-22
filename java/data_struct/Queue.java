public class Queue {

	char[] items;
	int putloc, getloc;

	Queue(int size) {
		items = new char[size];
		putloc = getloc = 0;
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
	public static void main(String[] args) {
		
		Queue bigQueue = new Queue(100);

		System.out.println("Using bigQueue to store the alphabet:");
		for (int i = 0; i < 26; i++) {
			bigQueue.put((char)('A' + i));
		}

		System.out.println("Contents of bigQueue: ");
		char ch;
		for (int i = 0; i < 26; i++) {
			ch = bigQueue.get();
			if (ch != (char)0) {
				System.out.print(ch);
			}
		}
		System.out.println();
	}
}