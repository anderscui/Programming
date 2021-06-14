package tour.java.concurrent;

public class Counter {
    private int i = 0;

    public synchronized int increment() {
        return i = i + 1;
    }

    public static void main(String[] args) throws InterruptedException {
        var c = new Counter();
        int REPEAT = 10_000_000;
        Runnable r = () -> {
            for (var i = 0; i < REPEAT; i++) {
                c.increment();
            }
        };

        Thread t1 = new Thread(r);
        Thread t2 = new Thread(r);

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("t1 is alive? " + t1.isAlive() + " state: " + t1.getState());

        var anomaly = (2 * REPEAT + 1) - c.increment();
        double percent = ((anomaly + 0.0) * 100) / (2 * REPEAT);
        System.out.println("Lost updates: " + anomaly + " ; % = " + percent);
    }
}
