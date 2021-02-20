package JAVA_Practice.OOP_9;

public class SuperLevel extends PlayerLevel{
    @Override
    public void run() {
        System.out.println("Run Super Fast");
    }

    @Override
    public void jump() {
        System.out.println("Jump Super High");
    }

    @Override
    public void turn() {
        System.out.println("Turn Turn Turn");
    }

    @Override
    public void showLevelMessage() {
        System.out.println("Level : High");
    }
}
