public class Help {
	public static void main(String[] args) throws java.io.IOException {
		System.out.println("Help on: ");
		System.out.println("\t 1.if");
		System.out.println("\t 2.switch");
		System.out.print("Choose one: ");

		char choose = (char)System.in.read();
		switch(choose) {
			case '1':
				System.out.println("The if: \n");
				System.out.println("if(condition) statement;");
				System.out.println("else statement");
				break;
			case '2':
				System.out.println("The switch: \n");
				System.out.println("switch(exp) {");
				System.out.println("	case constant: ");
				System.out.println("		statement sequence");
				System.out.println("		break;");
				System.out.println("	//...");
				System.out.println("}");
				break;
			default:
				System.out.println("Your choice is unknown for now.");
		}

	}
}
