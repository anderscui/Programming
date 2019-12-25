package andersc.tour.values.interops;

import org.jetbrains.annotations.Nullable;

public class Jhava {
    private int hitPoints = 123;
    private String greeting = "BLARGH";

    public static void main(String[] args) {
        System.out.println(Hero.makeProclamation());
        Hero.handOverFood();
    }

    @Nullable
    public String determineLevel() {
        return null;
    }

    public String utterGreeting() {
        return greeting;
    }

    public int getHitPoints() {
        return hitPoints;
    }

    public String getGreeting() {
        return greeting;
    }

    public void setGreeting(String value) {
        this.greeting = value;
    }
}
