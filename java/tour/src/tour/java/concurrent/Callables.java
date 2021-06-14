package tour.java.concurrent;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class Callables implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        return 123;
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        var c = new Callables();
        FutureTask<Integer> task = new FutureTask<>(c);

        var thread = new Thread(task);
        thread.start();
        System.out.println(task.get());
    }
}
