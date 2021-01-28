package JAVA_Practice.Datastructure;

import java.util.ArrayList;

public class Student {

    private int studentId;
    private String studentName;
    private ArrayList<Subject> subjectlist;

    public Student(int studentId, String studentName){
        this.studentId = studentId;
        this.studentName = studentName;

        subjectlist = new ArrayList<Subject>();
    }

    public void addSubject(String name, int score){
        Subject subject = new Subject();
        subject.setName(name);
        subject.setScorePoint(score);

        subjectlist.add(subject);
    }

    public void showStudentInfo(){
        int total = 0;

        for(Subject subject : subjectlist){
            total += subject.getScorePoint();

            System.out.println("학생 " + studentName + "님의 " + subject.getName() +
                    "과목의 성적은" + subject.getScorePoint() + "입니다.");
        }
        System.out.println("총점은 "+ total + "입니다.");
    }
}
