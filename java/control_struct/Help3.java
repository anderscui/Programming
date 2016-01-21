public class Help3 {
	public static void main(String[] args) throws java.io.IOException {
		
		char choose, ignore;

		while (true) {
			do {
				System.out.println("Help on: ");
				System.out.println("\t 1.if");
				System.out.println("\t 2.switch");
				System.out.println("\t 3.for");
				System.out.println("\t 4.while");
				System.out.println("\t 5.do-while");
				System.out.println("\t 6.break");
				System.out.println("\t 7.continue\n");
				System.out.print("Choose one (or press q to quit): ");

				choose = (char)System.in.read();
				do {
					ignore = (char)System.in.read();
				} while (ignore != '\n');
			} while ((choose < '1' | choose > '5') & (choose != 'q'));

			if (choose == 'q') {
				break;
			}

			System.out.println("\n");

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
			case '3':
				System.out.println("The for: \n");
				System.out.println("for(init; condition; iteration)");
				System.out.println("statement");
				break;
			case '4':
				System.out.println("The while: \n");
				System.out.println("while(condition) statement;");
				break;
			case '5':
				System.out.println("The do-while: \n");
				System.out.println("do {");
				System.out.println("	statement;");
				System.out.println("} while(condition);");
				break;
			case '6':
				System.out.println("The break: \n");
				System.out.println("break; or break label;");
				break;
			case '7':
				System.out.println("The continue: \n");
				System.out.println("continue; or continue label;");
				break;
			}
			System.out.println();
		}
	}
}