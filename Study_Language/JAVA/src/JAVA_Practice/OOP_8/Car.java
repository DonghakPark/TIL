package JAVA_Practice.OOP_8;

public abstract class Car {
    public abstract void drive();
    public abstract void stop();
    public abstract void wiper();


    public void washCar() {
    //필요한 경우에만 구현
    }

    public void startCar() {
        System.out.println("Turn On");
    }
    public void turnOff() {
        System.out.println("Turn Off");
    }

    // 항상 같은 시나리오 --> 템플릿 매서드 ( 시나리오를 정해놓는 것 )
    public final void run() {
        startCar();
        drive();
        wiper();
        stop();
        washCar();
        turnOff();

    }
}

