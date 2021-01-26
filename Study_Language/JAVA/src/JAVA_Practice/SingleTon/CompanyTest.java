package JAVA_Practice.SingleTon;

public class CompanyTest {

    public static void main(String[] args){
        Company c1 = Company.getInstance();

        Company c2 = Company.getInstance();

        System.out.println(c1);
        System.out.println(c2);
        //여러개가 생성되면 안되는 경우에 사용하는 패턴
        //private로 생성자, 객체를 생성하고 getInstance() method를 통해서 객체를 가져온다.

    }
}
