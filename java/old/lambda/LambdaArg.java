interface StringFunc {
	String func(String s);
}

public class LambdaArg {

	static String changeStr(StringFunc sf, String s) {
		return sf.func(s);
	}

	public static void main(String[] args) {
		String inStr = "Lambda Expressions Expand Java";
		String outStr;

		StringFunc reverse = str -> {
			String result = "";
			for (int i = str.length() - 1; i >= 0; i--) {
				result += str.charAt(i);
			}

			return result;
		};

		System.out.println("The string reversed: " + changeStr(reverse, inStr));
	}
}
