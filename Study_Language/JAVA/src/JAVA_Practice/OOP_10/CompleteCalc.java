package JAVA_Practice.OOP_10;

public class CompleteCalc extends Calculator{

    @Override
    public int times(int num1, int num2) {
        return num1 * num2;
    }

    @Override
    public int divide(int num1, int num2) {
        if ( num2 != 0){
            return num1 / num2;
        } else {
            return ERROR;
        }
    }

    public void showInfo() {
        System.out.println("Calc interface를 구현 했습니다.");
    }

}
