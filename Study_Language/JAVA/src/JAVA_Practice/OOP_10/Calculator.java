package JAVA_Practice.OOP_10;

public abstract class Calculator implements Calc{

    @Override
    public int add(int num1, int num2) {
        return num1 + num2;
    }

    @Override
    public int substract(int num1, int num2) {
        return num1 - num2;
    }

    @Override
    public void description() {
        System.out.println("완벽한 계산기 입니다.");
    }
}
