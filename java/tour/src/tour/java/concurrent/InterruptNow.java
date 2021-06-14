package tour.java.concurrent;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadLocalRandom;

public class InterruptNow {
    public static void main(String[] args) throws InterruptedException {
        ExecutorService executorService = Executors.newCachedThreadPool();
        executorService.execute(() -> {
            try {
                var randomMs = ThreadLocalRandom.current().nextInt(470, 491);
                System.out.println("Thread sleep:" + randomMs);
                Thread.sleep(randomMs);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread.sleep(500);
        executorService.shutdownNow();
        System.out.println("Main run");
    }
}
