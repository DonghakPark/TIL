package JAVA_Practice.OOP_9;

public class BeginnerLevel extends PlayerLevel {
    @Override
    public void run() {
        System.out.println("Run Slow");
    }

    @Override
    public void jump() {
        System.out.println("I Dont Know");
    }

    @Override
    public void turn() {
        System.out.println("I Dont Know");
    }

    @Override
    public void showLevelMessage() {
        System.out.println("Level : Beginner");
    }
}
