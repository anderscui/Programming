public class KbIn {
	public static void main(String[] args) 
		throws java.io.IOException {
		
		System.out.print("Press a key followed by ENTER: ");
		char ch = (char)System.in.read();
		System.out.println("Your key is: " + ch);
	}
}