public class GalToLitTable {
	public static void main(String[] args) {

		double gallons, liters;
		int counter;
		for (counter = 0, gallons = 1; gallons <= 10; gallons++) {
			liters = gallons * 3.7854;
			System.out.println(gallons + " gallons is " + liters + " liters.");

			counter++;
		}
	}
}
