public class Scope {
	public static void main(String[] args) {
		int i = 0;
        {
            i = 1;
        }
        System.out.println(i);
	}
}
