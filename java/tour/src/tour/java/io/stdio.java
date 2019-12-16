package tour.java.io;

import java.io.Console;
import java.util.Scanner;

public class stdio {
    public static void main(String[] args) {
//        Scanner in = new Scanner(System.in);
//        System.out.println("What's you name?");

//        // or next() for word;
//        String name = in.nextLine();
//        System.out.println(name);
//
//        System.out.println("Then, " + name + ", how many countries have you went to?");
//        int numCountries = in.nextInt();
//        System.out.println(numCountries);

        // now use console class to read password

//        doesn't work in an IDE.
//        Console terminal = System.console();
//        String username = terminal.readLine("User name: ");
//        char[] password = terminal.readPassword("Password: ");
//        System.out.println(username);
//        System.out.println(password);

        // formatting output
        System.out.printf("%8.2f", 1000.0/3.0);
    }
}
