package tour.java.basic;

import java.util.logging.Level;
import java.util.logging.Logger;

public class logging {
    private static Logger mainLogger = Logger.getLogger("tour.java");

    public static void main(String[] args) {
        Logger logger = Logger.getGlobal();
        logger.setLevel(Level.ALL);

        String filename = "test.pdf";
        logger.info("Opening file " + filename);

        mainLogger.setLevel(Level.ALL);
        mainLogger.info("A tour in java");

        method(filename, "*.pdf");
    }

    private static int method(String file, String pattern) {
        mainLogger.entering("tour.java", "logging",
                new Object[] {file, pattern});

        int count = 100;
        mainLogger.exiting("tour.java", "logging", count);
        return count;
    }
}
