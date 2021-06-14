package tour.java.concurrent;

public class Interruptions {
    private static class MyThread1 extends Thread {
        @Override
        public void run() {
            try {
                Thread.sleep(2000);
                System.out.println("Thread run");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Thread t1 = new MyThread1();
        t1.start();
        t1.interrupt();
        System.out.println("Main run");
    }
}
