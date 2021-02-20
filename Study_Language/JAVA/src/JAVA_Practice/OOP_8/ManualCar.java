package JAVA_Practice.OOP_8;

public class ManualCar extends Car{
    @Override
    public void drive() {
        System.out.println("Drive Person");
    }

    @Override
    public void stop() {
        System.out.println("Stop Person");
    }

    @Override
    public void wiper() {
        System.out.println("Wipe Manual");
    }
}
