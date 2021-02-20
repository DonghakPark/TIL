package JAVA_Practice.OOP_9;

public abstract class PlayerLevel {

    public abstract void run();
    public abstract void jump();
    public abstract void turn();
    public abstract void showLevelMessage();

    final public void go(int count) {
        System.out.println("-------------------------------");
        run();
        for (int i =0; i < count; i ++) {
            jump();
        }
        turn();
        System.out.println("-------------------------------");
    }

}
