public interface Containment<T> {
	boolean contains(T item);
}

class MyClass<T> implements Containment<T> {
	
	T[] arr;

	MyClass(T[] arr) {
		this.arr = arr;
	}

	public boolean contains(T item) {
		for (T i: arr) {
			if (i.equals(item)) {
				return true;
			}
		}
		return false;
	}
}

class GenInterfaceTest {
	public static void main(String[] args) {
		Integer arr[] = { 1, 2, 3 };
		MyClass<Integer> mc = new MyClass<Integer>(arr);
		System.out.println("Contains 2? " + mc.contains(2));
		System.out.println("Contains 5? " + mc.contains(5));
	}
}