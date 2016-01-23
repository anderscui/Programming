package bookpackext;

import bookpack.*;

class UseBook {
	public static void main(String[] args) {
		Book[] books = new Book[5];
		books[0] = new Book("Java Beginner's Guide", "Schildt", 2014);
		books[1] = new Book("Java Complete Ref", "Schildt", 2014);
		books[2] = new Book("The Art of Java", "Schildt and Holmes", 2003);
		books[3] = new Book("Red Storm Rising", "Clancy", 1986);
		books[4] = new Book("On the Road", "Kerouac", 1955);

		for (Book b : books) {
			b.show();
		}
	}
}
