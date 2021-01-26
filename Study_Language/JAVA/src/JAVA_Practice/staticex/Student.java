package JAVA_Practice.staticex;

public class Student {

    static int serialNum = 10000;

    int studentID;
    String studentName;

    public Student() {
        this.studentID = ++serialNum;
    }

    public static void getSerialNum() {
        int i = 10;

        i++;
        System.out.println(i);

        // 아래는 멤버(instance) 변수이기 때문에 static에서 사용할 수 없음
        //studentName = "홍길동";
    }
}
