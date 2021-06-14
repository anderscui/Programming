package tour.java.concurrent;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class WaitNotifyThreads {
    public synchronized void before() {
        System.out.println("before");
        notifyAll();
    }

    public synchronized void after() {
        try {
            wait();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("after");
    }

    public static void main(String[] args) throws InterruptedException {
        ExecutorService executorService = Executors.newCachedThreadPool();
        WaitNotifyThreads example = new WaitNotifyThreads();
        // two diff notations.
        executorService.execute(example::after);
        executorService.execute(example::before);
        // executorService.execute(() -> example.after());
        // executorService.execute(() -> example.before());

        executorService.shutdown();
        var terminated = executorService.awaitTermination(500, TimeUnit.MILLISECONDS);
        System.out.println("terminated? " + terminated);
    }
}
