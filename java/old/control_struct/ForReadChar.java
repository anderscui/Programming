public class ForReadChar {
	public static void main(String[] args) throws java.io.IOException {

		System.out.print("Press S to stop: ");

		for (int i = 0; (char)System.in.read() != 'S'; i++) {
			System.out.println("Pass #" + i);
		}
	}
}
