package JAVA_Practice.Datastructure;

public class Test_0128 {
    public static void main(String[] args) {
        Student studentLee = new Student(1001, "Lee");
        studentLee.addSubject("국어", 100);
        studentLee.addSubject("영어", 85);

        studentLee.showStudentInfo();

        Student studentKim = new Student(1002, "Kim");
        studentKim.addSubject("국어", 60);
        studentKim.addSubject("영어", 50);

        studentKim.showStudentInfo();
    }
}
