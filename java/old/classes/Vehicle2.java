// Add methods
public class Vehicle2 {

	int passengers;
	int fuelcap;
	int mpg;

	int range() {
		return fuelcap * mpg;
	}

	double fuelNeeded(int miles) {
		return (double)miles / mpg;
	}
}

class VehicleDemo {

	public static void main(String[] args) {
		Vehicle2 minivan = new Vehicle2();
		minivan.passengers = 7;
		minivan.fuelcap = 16;
		minivan.mpg = 21;

		System.out.println("Minivan can carry " + minivan.passengers + " with a range of " + minivan.range() + " miles.");

		int dist = 252;
		double gallons = minivan.fuelNeeded(dist);
		System.out.println("To go " + dist + " miles minivan needs " + gallons + " gallons of fuel.");
	}
}