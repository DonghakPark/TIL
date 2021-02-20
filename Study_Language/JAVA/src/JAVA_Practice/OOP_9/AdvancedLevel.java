package JAVA_Practice.OOP_9;

public class AdvancedLevel extends PlayerLevel{
    @Override
    public void run() {
        System.out.println("Run fast");
    }

    @Override
    public void jump() {
        System.out.println("jump high");
    }

    @Override
    public void turn() {
        System.out.println("I Dont Know");
    }

    @Override
    public void showLevelMessage() {
        System.out.println("Level : Middle");
    }
}
