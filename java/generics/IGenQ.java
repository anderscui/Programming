public interface IGenQ<T> {
	void put(T item) throws QueueFullException;
	T get() throws QueueEmptyException;
}