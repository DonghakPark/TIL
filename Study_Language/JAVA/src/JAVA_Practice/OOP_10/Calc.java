package JAVA_Practice.OOP_10;

public interface Calc {

    // interface는 추상 메서드와 상수만 선언할 수 있다.
    public static final double PI = 3.14;
    public static int ERROR = -9999999;

    abstract int add(int num1, int num2);
    abstract int substract(int num1, int num2);
    abstract int times(int num1, int num2);
    abstract int divide(int num1, int num2);

    default void description() {
        System.out.println("정수 계산기를 구현합니다.");
    }

    static int total(int[] arr){
        int total = 0;

        for(int i : arr){
            total += i;
        }
        return total;
    }
}
