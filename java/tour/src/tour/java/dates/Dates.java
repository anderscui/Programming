package tour.java.dates;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.Date;

public class Dates {
    public static void main(String[] args) {
        // showOldDate();
        // showNewDateAndTime();

        showNewDateTime();
    }

    private static void showNewDateTime() {
        LocalDateTime now = LocalDateTime.now();
        System.out.println(now);
    }

    private static void showOldDate() {
        // bad old Date class.
        Date date = new Date(117, 8, 21);
        System.out.println(date);
    }

    private static void showNewDateAndTime() {
        // use new ones
        LocalDate someday = LocalDate.of(2017, 9, 21);
        System.out.println(someday.getYear() + "/" + someday.getMonthValue() + "/" + someday.getDayOfMonth());

        // LocalDate now = LocalDate.now();

        // time
        LocalTime time = LocalTime.of(10, 11, 12);
        System.out.println(time.getHour() + " / " + time.getMinute() + " / " + time.getSecond());

        // parse
        someday = LocalDate.parse("2017-09-21");
        time = LocalTime.parse("09:01:59");
    }
}
