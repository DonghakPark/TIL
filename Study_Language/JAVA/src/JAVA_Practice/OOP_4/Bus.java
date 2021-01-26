package JAVA_Practice.OOP_4;

public class Bus {

    int busNumber;
    int passengerCount;
    int money;

    public Bus(int busNumber) {
        this.busNumber = busNumber;
    }

    public void take(int money){
        this.passengerCount++;
        this.money += money;
    }
    public void showInfo() {
        System.out.println("버스"+ busNumber + "번의 승객은 " + passengerCount + "명이고 수입은" + money +  "입니다.");
    }
}
