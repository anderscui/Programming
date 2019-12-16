class Block {
	int a, b, c;
	int volume;

	Block(int a, int b, int c) {
		this.a = a;
		this.b = b;
		this.c = c;

		volume = a * b * c;
	}

	boolean sameBlock(Block other) {
		return (other.a == a) && (other.b == b) && (other.c == c);
	}

	boolean sameVolume(Block other) {
		return (other.volume == volume);
	}
}

public class PassObj {
	public static void main(String[] args) {

		Block b1 = new Block(10, 2, 5);
		Block b2 = new Block(10, 2, 5);
		Block b3 = new Block(4, 5, 5);

		System.out.println("Is b1 same as b2? " + b1.sameBlock(b2));
		System.out.println("Is b1 same as b3? " + b1.sameBlock(b3));
		System.out.println("Is b1 same volume as b3? " + b1.sameVolume(b3));
	}
}
