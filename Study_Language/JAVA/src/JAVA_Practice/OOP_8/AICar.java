package JAVA_Practice.OOP_8;

public class AICar extends Car{
    @Override
    public void drive() {
        System.out.println("Auto Drive");
    }

    @Override
    public void stop() {
        System.out.println("Auto Stop");
    }

    @Override
    public void wiper() {
        System.out.println("Auto Wipe");
    }

    @Override
    public void washCar() {
        System.out.println("Auto Wash");
    }
}
