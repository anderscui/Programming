public class WhilePowersOfTwo {
	public static void main(String[] args) {
		int N = Integer.parseInt(args[0]);

		int v = 1;
		int i = 0;
		while (i <= N) {
			System.out.println(i + " " + v);
			i++;
			v *= 2;
		}
	}
}
