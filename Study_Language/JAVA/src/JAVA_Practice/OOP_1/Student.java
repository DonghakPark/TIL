package JAVA_Practice.OOP_1;

//클래스 밖에는 패키지와 import 내용만 쓴다.

public class Student {

    //Java Naming Comvention : Class는 대문자로 시작 -> 퍼블릭 클래스는 하나여야 하고 자바 코드 이름과 같아야 한다.
    //메소드, 변수 등 처음에는 소문자로 시작하고 단어의 첫 글자는 대문자로 표시

    int studentID;
    String studentName;
    int grade;
    String address;

    //기본 생성자 : 처음 객체를 생성하면서 해야할 일들을 만드는 것
    public Student(){

        this.studentID = 00;
        this.studentName = "NULL";
    }

    public Student(int id, String name){
        this.studentName = name;
        this.studentID = id;
    }

    public void showStudentInfo() {
        System.out.println(studentName + "," + address);
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

//    public static void main(String[] args) {
//        Student studentLee = new Student();
//        studentLee.studentName = "이순신";
//        studentLee.address = "서울시 서초구 서초동";
//
//        studentLee.showStudentInfo();
//    }

    //JVM이 메인 함수를 호출함 ( 있는 경우 )
    public static void main(String[] args) {

        Student studentLee = new Student();
        //studentLee -> 참조 변수이다.

        studentLee.studentName = "이순시";
        studentLee.studentID = 100;
        studentLee.address = "서울시 영등포구 여의도동";

        Student studentKim = new Student();
        studentKim.studentName = "김유신";
        studentKim.studentID = 101;
        studentKim.address = "서울시 영등포구 강남";

        studentKim.showStudentInfo();
        studentLee.showStudentInfo();

        Student studentPark = new Student();
        studentPark.showStudentInfo();

        }

    }

