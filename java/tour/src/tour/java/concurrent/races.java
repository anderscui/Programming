package tour.java.concurrent;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class races {

    public static void main(String[] args) {
        AtomicInteger count = new AtomicInteger();

        ExecutorService executor = Executors.newCachedThreadPool();
        for (int i = 1; i <= 100; i++) {
            int taskId = i;
            Runnable task = () -> {
                for (int j = 1; j <= 1000; j++) {
                    count.getAndIncrement();
                }
                System.out.println(taskId + ": " + count);
            };
            executor.execute(task);
        }
    }
}
