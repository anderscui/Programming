package tour.java.patterns.singleton;

public class Singleton {
    private final static Singleton instance = new Singleton();
    private static boolean initialized = false;

    private Singleton() {
        super();
    }

    private void init() {}

    public static synchronized Singleton getInstance() {
        if (initialized)
            return instance;

        instance.init();
        initialized = true;
        return instance;
    }
}
