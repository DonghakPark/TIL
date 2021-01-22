package JAVA_Practice.OOP_2;

public class StudentTest {
    public static void main(String[] args) {

        Student studentJames = new Student(100, "James");
        studentJames.setKorea("국어", 100);
        studentJames.setMath("수학", 20);
        studentJames.showStudentInfo();
    }
}
