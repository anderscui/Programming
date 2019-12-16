class GenQueueTest {
	public static void main(String[] args) {
		Integer[] items = new Integer[5];
		GenQueue<Integer> iq = new GenQueue<Integer>(items);

		System.out.println("A queue of integers.");
		try {
			for (int i = 0; i < 6; i++) {
				System.out.println("Adding " + i + " to queue.");
				iq.put(i);
			}
		}
		catch (QueueFullException qfe) {
			System.out.println(qfe);
		}
		System.out.println();

		try {
			for (int i = 0; i < 6; i++) {
				System.out.println("Getting next item from queue.");
				System.out.println(iq.get());
			}
		}
		catch (QueueEmptyException qee) {
			System.out.println(qee);
		}
		System.out.println();
	}
}