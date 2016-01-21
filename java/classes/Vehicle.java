// Define a simple class
public class Vehicle {

	int passengers;
	int fuelcap;
	int mpg;

	Vehicle(int p, int f, int m) {
		passengers = p;
		fuelcap = f;
		mpg = m;
	}

	int range() {
		return mpg * fuelcap;
	}

	double fuelNeeded(int miles) {
		return (double)miles / mpg;
	}
}

class VehicleDemo {

	public static void main(String[] args) {
		Vehicle minivan = new Vehicle(7, 16, 21);

		int range = minivan.fuelcap * minivan.mpg;
		System.out.println("Minivan can carry " + minivan.passengers + " with a range of " + range);
	}
}