package JAVA_Practice.SingleTon;

public class Company {

    private static Company instance = new Company();

    //외부에서 이 constructor를 생성할 수 없음
    private Company(){

    }

    public static Company getInstance() {
        if(instance == null)
            instance = new Company();
        return instance;
    }
}
