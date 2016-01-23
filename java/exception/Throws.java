public class Throws {

	public static char prompt(String msg) throws java.io.IOException {
		System.out.print(msg + ": ");
		return (char) System.in.read();
	}

	public static void main(String[] args) {
		char ch;
		try {
			ch = prompt("Enter a letter");
		}
		catch (java.io.IOException ex) {
			System.out.println("I/O excetion occurred.");
			ch = 'X';
		}
		System.out.println("You pressed " + ch);
	}
}