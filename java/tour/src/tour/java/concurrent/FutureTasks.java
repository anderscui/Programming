package tour.java.concurrent;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class FutureTasks {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        var task1 = new FutureTask<>(() -> {
            var result = 0;
            for (int i = 1; i <= 100; i++) {
                Thread.sleep(10);
                result += i;
            }
            return result;
        });
        Thread thread1 = new Thread(task1);
        thread1.start();

        Thread thread2 = new Thread(() -> {
            System.out.println("another thread is running...");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        thread2.start();

        System.out.println(task1.get());
    }
}
