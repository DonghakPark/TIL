package JAVA_Practice.OOP_2;

public class Student {

    int studentID;
    String studentName;

    Subject korea;
    Subject math;

    public Student() {
        this.korea = new Subject();
        this.math = new Subject();

    }

    public Student(int id, String name) {
        this.studentID = id;
        this.studentName = name;

        this.korea = new Subject();
        this.math = new Subject();
    }

    public void setKorea(String name, int score) {
        korea.setSubjectName(name);
        korea.setScore(score);
    }

    public void setMath(String name, int score) {
        math.setSubjectName(name);
        math.setScore(score);
    }

    public void showStudentInfo() {
        int total = korea.getScore() + math.getScore();
        System.out.println(studentName + " 학색의 총점은 " + total + "입니다.");

    }
}
