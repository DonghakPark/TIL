package JAVA_Practice.OOP_1;

public class StudentTest {
    public static void main(String[] args) {

        Student studentLee = new Student(); //class 생성

        studentLee.studentName = "이순신";
        studentLee.address = "서울시 서초구 서초동";

        studentLee.showStudentInfo();
        int num1 = 10;
        int num2 = 20;
        int sum = FunctionTest.addNum(num1, num2);
        System.out.println(sum);
    }



}
