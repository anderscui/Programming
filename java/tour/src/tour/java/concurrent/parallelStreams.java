package tour.java.concurrent;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Random;
import java.util.concurrent.TimeUnit;

public class parallelStreams {
    private static String genRandomString() {
        int left = 97;
        int right = 122;
        int targetLen = 2;

        Random random = new Random();
        StringBuilder buffer = new StringBuilder(targetLen);
        for (int i = 0; i < targetLen; i++) {
            int randomInt = left + (int)(random.nextFloat() * (right - left + 1));
            buffer.append((char)randomInt);
        }
        return buffer.toString();
    }

    public static void main(String[] args) {
        List<String> coll = new ArrayList<>();
        for (int i = 0; i <= 50000000; i++) {
            coll.add(genRandomString());
        }
        //System.out.println(coll);

        long start = new Date().getTime();
        long result = coll.parallelStream().filter(s -> s.startsWith("a")).count();
        long end = new Date().getTime();
        // System.out.println(TimeUnit.MICROSECONDS.toSeconds(end-start));
        System.out.println(end-start);
        System.out.println(result);

        start = new Date().getTime();
        result = 0;
        for (String s: coll) {
            if (s.startsWith("a")){
                result += 1;
            }
        }
        end = new Date().getTime();
        System.out.println(end-start);
        System.out.println(result);
    }
}
