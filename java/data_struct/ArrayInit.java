public class ArrayInit {
	public static void main(String[] args) {
		
		int[][] squares = {
			{ 1, 1 },
			{ 2, 4 },
			{ 3, 9 },
			{ 4, 16 },
			{ 5, 25 },
		};

		for (int i = 0; i < squares.length; i++) {
			for (int j = 0; j < 2; j++) {
				System.out.print(squares[i][j] + " ");
			}
			System.out.println();
		}
	}
}
