public class Gen<T> {
	T obj;

	Gen(T o) {
		obj = o;
	}

	T getObj() {
		return obj;
	}

	void showType() {
		System.out.println("Type of T is " + obj.getClass().getName());
	}
}

class GenTest {
	public static void main(String[] args) {
		Gen<Integer> intObj;
		intObj = new Gen<Integer>(10);
		intObj.showType();
		System.out.println("Value: " + intObj.getObj());

		System.out.println();

		Gen<String> strObj = new Gen<String>("Hello");
		strObj.showType();
		System.out.println("Value: " + strObj.getObj());
	}
}