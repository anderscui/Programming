// similar with C# static constructor.
public class StaticBlock {
	static double rootOf2;
	static double rootOf3;

	static {
		System.out.println("Inside statick block.");
		rootOf2 = Math.sqrt(2.0);
		rootOf3 = Math.sqrt(3.0);
	}

	StaticBlock(String msg) {
		System.out.println(msg);
	}
}

class StaticBlockDemo {
	public static void main(String[] args) {
		StaticBlock sb = new StaticBlock("Inside ctor");
		System.out.println("Squre root of 2 is " + StaticBlock.rootOf2);
		System.out.println("Squre root of 3 is " + StaticBlock.rootOf3);
	}
}
