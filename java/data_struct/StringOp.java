public class StringOp {
	public static void main(String[] args) {
		
		String str1 = "Hello World!";
		String str2 = new String("Java strings are objects.");
		String str3 = new String(str2);

		// length()
		System.out.println("str1: " + str1);
		System.out.println("its length is " + str1.length());

		// charAt()
		for (int i = 0; i < str1.length(); i++) {
			System.out.print(str1.charAt(i));
		}
		System.out.println();

		// equals()
		if (str1.equals(str2)) {
			System.out.println("str1 equals str2");
		} else {
			System.out.println("str1 does not equal str2");
		}

		// compareTo()
		int result = str1.compareTo(str2);
		if (result == 0) {
			System.out.println("str1 and str2 are equal");
		} else if (result < 0) {
			System.out.println("less");
		} else {
			System.out.println("greater");
		}

		// assign new val
		str3 = "Because of a great love, one is courageous.";

		int idx = str3.indexOf("love");
		System.out.println(idx);

		idx = str3.indexOf("hate"); 
		System.out.println(idx); // -1	

		// sub string
		idx = str3.indexOf("love");
		System.out.println(str3.substring(idx, idx + "love".length())); // different with SubString in C#.
	}
}
