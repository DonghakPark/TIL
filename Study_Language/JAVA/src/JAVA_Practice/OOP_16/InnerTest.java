package JAVA_Practice.OOP_16;

class OuterClass {

    private int num = 10;
    private static int sNum = 20;
    private InClass inClass;

    public OuterClass() {
        inClass = new InClass();
    }

    class InClass{
        int inNum = 200;

        void inTest() {
            System.out.println(num);
            System.out.println(sNum);
        }

    }
    public void usingTest() {
        inClass.inTest();
    }

}

public class InnerTest {
    public static void main(String[] args) {
        OuterClass outerClass = new OuterClass();
        outerClass.usingTest();
    }
}