package JAVA_Practice.OOP_3;

class Birthday{
    int day;
    int month;
    int year;

    public void setYear(int year){
        this.year = year;
    }

    public void printThis(){
        System.out.println(this);
    }
}

public class ThisExample {
    public static void main(String[] args){
        Birthday test = new Birthday();
        test.setYear(2020);
        test.printThis();

        Birthday test2 = new Birthday();
        test2.setYear(2020);
        test2.printThis();

    }
}
