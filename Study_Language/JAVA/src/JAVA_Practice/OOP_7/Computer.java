package JAVA_Practice.OOP_7;

public abstract class Computer {

    //각각의 상속받은 객체가 구체적으로 구현해야 할 때 추상 메서드를 사용한다.
    //즉 사용되는 기능이지만 구체적으로 상위 클래스에서는 정하기 힘든 경우에 사용한다.
    //이를 구현을 위임했다고 한다.
    public abstract void display();
    public abstract void typing();


    public void turnOn() {
        System.out.println("TurnOn the Power");
    }

    public void turnOff() {
        System.out.println("TurnOff the Power");
    }

}
