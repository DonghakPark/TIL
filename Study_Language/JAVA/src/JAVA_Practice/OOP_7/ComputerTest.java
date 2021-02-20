package JAVA_Practice.OOP_7;

public class ComputerTest {
    public static void main(String[] args) {
        // 아래와 같이 추상클래스는 사용할 수 없음
        //Computer c1 = new Computer();

        // 추상 클래스라 생성 불가
        //Computer c2 = new NoteBook();

        Computer c1 = new DeskTop();
        Computer c2 = new MyNoteBook();
        NoteBook c3 = new MyNoteBook();




    }
}
