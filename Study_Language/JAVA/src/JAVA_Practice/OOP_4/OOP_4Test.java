package JAVA_Practice.OOP_4;

public class OOP_4Test {
    public static void main(String[] args){
        //학생 1,2
        Student james = new Student("James", 5000);
        Student tomas = new Student("Tomas", 10000);

        // Bus 1
        Bus bus100 = new Bus(100);

        james.takeBus(bus100);
        james.showInfo();
        bus100.showInfo();

        Subway subwayGreen = new Subway(2);
        tomas.takeSubway(subwayGreen);
        tomas.showInfo();
        subwayGreen.showInfo();

    }
}
