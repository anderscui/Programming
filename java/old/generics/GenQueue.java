class GenQueue<T> implements IGenQ<T> {

	private T[] items;
	private int putloc, getloc;

	GenQueue(T[] arr) {
		items = arr;
		putloc = getloc = 0;
	}

	public void put(T item) throws QueueFullException {
		if (putloc == items.length) {
			throw new QueueFullException(items.length);
		}

		items[putloc++] = item;
	}

	public T get() throws QueueEmptyException {
		if (getloc == putloc) {
			throw new QueueEmptyException();
		}

		return items[getloc++];
	}
}