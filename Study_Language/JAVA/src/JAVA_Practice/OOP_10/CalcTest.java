package JAVA_Practice.OOP_10;

public class CalcTest {

    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 2;

        Calc calc = new CompleteCalc();

        System.out.println(calc.add(num1, num2));
        System.out.println(calc.substract(num1, num2));
        System.out.println(calc.times(num1, num2));
        System.out.println(calc.divide(num1, num2));

        int[] arr = {1, 2, 3, 4, 5, 6};
        int sum = Calc.total(arr);
        System.out.println(sum);

    }
}
